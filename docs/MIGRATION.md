# 历史与完整性验证

当前环境没有 git-subtree 扩展，因此本次采用等效的双父提交子树合并：`git merge -s ours --no-commit --no-ff --allow-unrelated-histories` 后 `git read-tree --prefix=目录/ -u 原始SHA` 并提交。没有压缩或改写原始提交。每个源仓库保持完整独立目录，内部文件、文件模式、Git 对象 SHA 和相对路径不变。

`source/<原仓库>/<原分支>` 保存原始分支引用；`main` 的合并祖先包含原始默认分支历史。原始提交发生于原仓库根路径，查询迁移前历史请使用源分支或原始 SHA；不要只通过新路径的 `git log --follow` 判断历史是否存在。

详见 [逐文件清单](migration-manifest.json)。使用仓库内的验证脚本：

```bash
python3 scripts/verify_migration.py
git log --all --graph --oneline
```

验证脚本检查每个子目录的 Git 树 SHA、全部原始提交对象与源分支引用、原 HEAD 祖先关系、package.json 和锁文件、ZIP 校验及文档相对链接。文件 SHA 验证包含二进制数据、许可证和文档。

六个源仓库均无 Git 子模块；迁移时未发现 Git LFS 指针。原 Issues、Stars、fork 关系、仓库设置不会通过 subtree 合入新仓库；它们应留在原仓库，待验收后再经用户确认转移原仓库至归档组织。

MATLAB 与旧 Vue 工程的运行正确性需要独立验证；文件迁移通过不代表算法或应用运行通过。没有批量升级依赖，没有修改后端接口或部署配置。
