import pathlib, subprocess, json, re, zipfile
from urllib.parse import unquote, urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'docs/migration-manifest.json').read_text())
def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args],text=True).strip()
for source in manifest['sources']:
    prefix=source['prefix'];sha=source['head_sha']
    assert git('rev-parse','HEAD:'+prefix)==source['tree_sha'],prefix+' tree differs'
    assert int(git('ls-tree','-r','--name-only','HEAD:'+prefix).count('\n'))+1==source['file_count']
    git('merge-base','--is-ancestor',sha,'HEAD')
    assert git('rev-parse','refs/heads/source/'+source['repository'].split('/')[1]+'/'+source['default_branch'])==sha
    for commit in source['commit_shas']: git('cat-file','-e',commit+'^{commit}')
    for package in source['package_manifests']:
        json.loads((ROOT/prefix/package['path']).read_text())
        for lock in package['lockfiles']: assert (ROOT/prefix/lock).is_file()
    for path in source['data_files']:
        if path.endswith('.zip'):
            with zipfile.ZipFile(ROOT/prefix/path) as z: assert z.testzip() is None
    print(source['repository'],source['file_count'],'files,',source['commit_count'],'commits: PASS')
for doc in [ROOT/'README.md',ROOT/'docs/MIGRATION.md',ROOT/'docs/VALIDATION.md']:
    text=doc.read_text()
    for href in re.findall(r'\]\(([^)]+)\)',text):
        parsed=urlsplit(href)
        if parsed.scheme or href.startswith('#'): continue
        assert (doc.parent/unquote(parsed.path)).exists(),str(doc)+' broken link: '+href
assert not git('status','--porcelain'), 'Working tree not clean'
print('Top-level documentation links and clean working tree: PASS')
