# GitHub 仓库整理最终验收报告

2026-10-14（北京时间）。**个人账号 liujunyukarry 已从原来的 10 个仓库精简为 6 个。** 创建两个综合仓库后曾为 12 个；六个完整旧仓库转入独立归档组织并设为只读，因此个人账号最终剩 6 个。没有删除任何原始仓库。

## 最终个人仓库

| 仓库 | 可见性 | 本次处理 |
| --- | --- | --- |
| [vue-admin-labs](https://github.com/liujunyukarry/vue-admin-labs) | 公开 | 三个 Vue 原仓库完整独立目录合并，保留历史 |
| [sar-algorithm-labs](https://github.com/liujunyukarry/sar-algorithm-labs) | 公开 | 三个 SAR 小型原仓库完整独立目录合并，保留历史 |
| 原有私有仓库（名称不公开） | 私有 | 文件、默认分支、可见性保持原样 |
| [sar](https://github.com/liujunyukarry/sar) | 公开 | 大型仓库独立保留，未参与合并 |
| [uk-business-english](https://github.com/liujunyukarry/uk-business-english) | 公开 | 文件、页面路径与任务配置未修改 |
| [claude-english](https://github.com/liujunyukarry/claude-english) | 公开 | 文件、页面路径未修改 |

个人仓库数量同时通过已连接 GitHub 的 owner 过滤清单（6 条）和 GitHub 个人主页 Repositories (6) 核实。公开主页显示 5 个公开仓库；原有私有仓库继续保持私有。

## 原仓库对应目录与最终状态

| 原仓库 | 新综合仓库中的完整目录 | 原仓库最终位置 | 原始文件数 | 原始提交数 |
| --- | --- | --- | --- | --- |
| `vue2_3` | `vue-admin-labs/mixed-vue/vue2_3/` | [只读归档](https://github.com/liujunyukarry-archive/vue2_3) | 162 | 3 |
| `vue3-backendmanagementsystem` | `vue-admin-labs/vue3/vue3-backendmanagementsystem/` | [只读归档](https://github.com/liujunyukarry-archive/vue3-backendmanagementsystem) | 30 | 3 |
| `vue3-2_backendmanagementsystem` | `vue-admin-labs/vue3.2-resources/vue3-2_backendmanagementsystem/` | [只读归档](https://github.com/liujunyukarry-archive/vue3-2_backendmanagementsystem) | 43 | 3 |
| `Radar-SAR-simu` | `sar-algorithm-labs/radar-basics/Radar-SAR-simu/` | [只读归档](https://github.com/liujunyukarry-archive/Radar-SAR-simu) | 9 | 5 |
| `SAR-imaging` | `sar-algorithm-labs/imaging-algorithms/SAR-imaging/` | [只读归档](https://github.com/liujunyukarry-archive/SAR-imaging) | 36 | 7 |
| `Simulation-of-SAR-Imaging-Algorithm` | `sar-algorithm-labs/point-targets/Simulation-of-SAR-Imaging-Algorithm/` | [只读归档](https://github.com/liujunyukarry-archive/Simulation-of-SAR-Imaging-Algorithm) | 7 | 4 |

六个旧仓库均保持原名、公开可见、只读归档，归属于 liujunyukarry-archive，不再计入个人账号。归档组织采用 Free 方案，GitHub 已确认只有 liujunyukarry 一名成员且为所有者；没有邀请其他人。

## 文件与历史完整性

- 原始文件合计 287 个（Vue 235、SAR 52），原始提交合计 25 个（Vue 9、SAR 16）。
- 每个迁入目录的完整 Git 树 SHA 与迁移前默认分支树完全一致，验证包含源码、二进制数据、图片、ZIP、独立 package.json/锁文件、原始文档、许可文本和文件模式。
- 使用等效的无压缩子树合并：双父提交保留原始祖先，未改写原始提交；源分支独立保留为 source/<仓库>/<分支>。原始 author、committer、时间与 SHA 保持一致。
- 独立从目标 GitHub 远端取回后检查全部 25 个原始提交对象的完整字节，与原始镜像一致；树、分支、祖先关系、依赖清单、目录结构、顶层文档相对链接及 git fsck --full 通过。
- 原 vue2_3 内 Vue 2、Vue 2 + TypeScript、Vue 3 三套工程保持独立，没有合并不同版本的 src 或依赖文件；Vue 3.2 资源与 ZIP 模板保持原样，ZIP 109 个条目 CRC 校验通过。
- SAR 数据没有去重覆盖，MIT 与 Apache 2.0 原许可、作者信息保留；其余无独立 LICENSE 的项目未被额外赋予统一许可。
- 转移后六个原仓库 ID 与原 HEAD 均未改变；三个 SAR 原仓库的 fork 关系仍分别指向 lwh521jll/Radar-SAR-simu、joeyos/SAR-imaging、denkywu/Simulation-of-SAR-Imaging-Algorithm。

新仓库内 scripts/verify_migration.py 和只读 GitHub Actions 持续提供迁移完整性检查。只读工作流不安装应用依赖、不部署页面、不改动外部定时任务。

## 链接与部署核验

六个旧 GitHub 仓库网页地址都在云端浏览器中实际打开，均重定向至对应 liujunyukarry-archive 原名仓库，并显示只读横幅。六个旧 git URL 与新归档 git URL 的 ls-remote 均成功，返回的全部引用相同。

六个待迁移原库均未启用 GitHub Pages，公开元数据未见部署或 Release 记录，Webhook 设置均为空，应用安装列表只见 ChatGPT Codex Connector。原仓库的 GitHub ID、开放 Issues/PR 数（均 0）及 Stars（均 0）转移前后保持一致。

GitHub 官方说明仓库转移保留 Git 历史、Issues、PR、Wiki、Stars 与 fork 关系；仓库/Git 旧地址重定向，但 GitHub Pages 不自动重定向。六个原库没有 Pages；英语 Pages 仓库没有转移。今后不要在个人账号重新创建六个旧名称，避免移除原地址重定向。

依据：https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository

## 英语、AI 学习与其他保留仓库

整理前后 HEAD 一致：

- 原有私有仓库：HEAD 未变，名称及 SHA 不公开。
- sar: e80e4db7ab454a5a5743b2bea6777b8d21117df2
- uk-business-english: 2678a626420bb4bdc443f5d199bcb763fabdf1de
- claude-english: 8097ff51af2ad7bbb18475f8e8c3c28979998785

两个英语仓库的文件、页面路径、部署地址和设置本轮均没有写操作。英语总入口保持 https://liujunyukarry.github.io/uk-business-english/ 。

ChatGPT 自动化仍只有两条启用任务：英国出差英语口语 06:00、AI 每日学习 06:20，均为 Asia/Shanghai。开始与完成时对全部任务 prompt、schedule、is_enabled 逐项比较，完全一致；没有创建额外任务，没有修改任务提示词。

此核验证明本轮整理没有修改学习项目或任务，不代表未来通知投递与每期内容质量已得到保证。

## 真实运行限制

五个 Vue 工程在独立临时副本中使用 Node.js v24.19.0 / Yarn 1.22.22 尝试冻结锁文件安装，均在安装阶段因锁文件需要更新而失败，没有进入编译阶段。没有擅自修改锁文件或升级依赖，不能宣称应用构建成功。旧 node-sass 等依赖的兼容性需作为单独维护任务处理。

本环境未安装 MATLAB/Octave，未运行 SAR 算法，没有验证算法数值结果和百度网盘外部原始数据可下载性。

当前连接器对新组织的仓库枚举返回空列表，因此归档组织的数量以 GitHub 组织网页显示的 6 repositories 与六个仓库 ID/owner/archived 的逐库读取共同验收；这不影响旧库在 GitHub 网页和 Git 中实际访问。没有为此额外扩展应用权限。

仓库精简、资产保留、只读归档和旧地址重定向的任务已完成；旧工程依赖修复与算法运行验证没有混入此次整理。
