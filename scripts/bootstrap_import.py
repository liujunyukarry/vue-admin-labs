"""Run only in one new target repo; never write to an original repository."""
import json, pathlib, subprocess, os, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args],text=True).strip()
allowed={'liujunyukarry/vue-admin-labs','liujunyukarry/sar-algorithm-labs'}
repo=os.environ.get('GITHUB_REPOSITORY','')
assert repo in allowed,'Refusing to write outside the two requested new repositories'
manifest=json.loads((ROOT/'docs/migration-manifest.json').read_text())
assert not git('status','--porcelain'),'Working tree must be clean'
git('config','user.name','Karry Repository Maintenance')
git('config','user.email','54398473+liujunyukarry@users.noreply.github.com')
for source in manifest['sources']:
    origin=source['repository'];prefix=source['prefix'];sha=source['head_sha'];branch=source['default_branch']
    assert origin.startswith('liujunyukarry/') and origin not in allowed
    url='https://github.com/'+origin+'.git'
    observed=git('ls-remote',url,'refs/heads/'+branch).split()[0]
    assert observed==sha,'Source changed since audit; stop and re-audit '+origin
    git('fetch','--no-tags',url,'refs/heads/'+branch)
    assert git('rev-parse','FETCH_HEAD')==sha
    source_ref='source/'+origin.split('/')[1]+'/'+branch
    refcheck=subprocess.run(['git','-C',str(ROOT),'rev-parse','--verify','refs/heads/'+source_ref],capture_output=True,text=True)
    if refcheck.returncode==0: assert refcheck.stdout.strip()==sha
    else:git('branch',source_ref,sha)
    present=subprocess.run(['git','-C',str(ROOT),'rev-parse','--verify','HEAD:'+prefix],capture_output=True,text=True)
    if present.returncode==0: assert present.stdout.strip()==source['tree_sha']
    else:
        git('merge','-s','ours','--no-commit','--no-ff','--allow-unrelated-histories',sha)
        git('read-tree','--prefix='+prefix+'/','-u',sha)
        git('commit','-m','import: preserve complete '+origin+' history under '+prefix)
    assert git('rev-parse','HEAD:'+prefix)==source['tree_sha']
subprocess.run([sys.executable,str(ROOT/'scripts/verify_migration.py')],check=True)
git('fsck','--full')
# Check all six original heads again before publishing either target.
for source in manifest['sources']:
    observed=git('ls-remote','https://github.com/'+source['repository']+'.git','refs/heads/'+source['default_branch']).split()[0]
    assert observed==source['head_sha'],'Source changed during migration; stop'
if '--prepare-only' in sys.argv:
    print('Prepared and validated locally; no remote push performed.')
    sys.exit(0)
origin_url=git('remote','get-url','origin').removesuffix('.git').removesuffix('/')
assert origin_url=='https://github.com/'+repo,'Unexpected push destination'
refspecs=['HEAD:refs/heads/main']+['refs/heads/source/'+s['repository'].split('/')[1]+'/'+s['default_branch'] for s in manifest['sources']]
git('push','--atomic','origin',*refspecs)
print('Published main and preserved source branches; remote reread still required.')
