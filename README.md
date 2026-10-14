# Vue Admin Labs

Vue 2、Vue 2 + TypeScript、Vue 3 后台工程和 Vue 3.2 学习资源集合。三个原仓库完整迁入独立目录，源码与原始 Git 提交历史保留。此仓库没有统一的根级应用和依赖安装命令。

## 项目索引

| 分类 | 独立工程或资源目录 | 依赖声明 |
| --- | --- | --- |
| Vue 2 | [project-v2](mixed-vue/vue2_3/Vue_project/项目vue2+ts+vue3源码/project-v2/) | Vue `^2.6.11`，Vue CLI 4 |
| Vue 2 + TypeScript | [project-ts](mixed-vue/vue2_3/Vue_project/项目vue2+ts+vue3源码/project-ts/) | Vue `^2.6.11`，TypeScript `~4.1.5` |
| Vue 3 | [project-v3](mixed-vue/vue2_3/Vue_project/项目vue2+ts+vue3源码/project-v3/) | Vue `^3.0.0`，Vue CLI 4 |
| Vue 3 后台管理 | [code](vue3/vue3-backendmanagementsystem/code/) | Vue `^3.2.13`，Vue CLI 5 |
| Vue 3.2 学习资源 | [resource](vue3.2-resources/vue3-2_backendmanagementsystem/resource/) | 页面片段、接口文档、笔记、ZIP 模板 |

版本列来自原始 package.json 的范围声明，不代表已经锁定安装或测试的精确版本。`vue2_3` 的截图、版本切换文档、TypeScript 重构说明和接口资料都保留在 [Vue_project](mixed-vue/vue2_3/Vue_project/) 中。

## 运行独立工程

先按旧依赖选择兼容的 Node.js 与 Yarn 1 环境，再进入具体工程：

```bash
cd "mixed-vue/vue2_3/Vue_project/项目vue2+ts+vue3源码/project-v3"
yarn install --frozen-lockfile
yarn serve
# 构建：yarn build
# 静态检查：yarn lint
```

Vue 2 或 TypeScript 工程分别换成 `project-v2` 或 `project-ts`；另一后台工程进入 `vue3/vue3-backendmanagementsystem/code` 后执行相同命令。四个工程各自的 package.json 与 yarn.lock 保持原样，不能合并安装。

Vue 2 两个工程使用旧 `node-sass`，不能据此保证支持最新 Node.js。后台 API、登录功能和远程接口是否可用需另行验证。

Vue 3.2 资源先复制并解压 [vue_3.2.zip](vue3.2-resources/vue3-2_backendmanagementsystem/resource/模板/vue_3.2.zip) 到单独的工作目录。ZIP 内 package.json 声明 Vue `^3.2.8`，脚本为 `serve/build/lint`；检查其锁文件和 `prepare: husky install` 后再安装，不要在资源仓库根目录直接运行。

## 原仓库与许可

| 原仓库 | 完整保留目录 |
| --- | --- |
| liujunyukarry/vue2_3 | [mixed-vue/vue2_3](mixed-vue/vue2_3/) |
| liujunyukarry/vue3-backendmanagementsystem | [vue3/vue3-backendmanagementsystem](vue3/vue3-backendmanagementsystem/) |
| liujunyukarry/vue3-2_backendmanagementsystem | [vue3.2-resources/vue3-2_backendmanagementsystem](vue3.2-resources/vue3-2_backendmanagementsystem/) |

三个源仓库未发现独立 LICENSE 文件；此次没有替原作者授予新许可。原始说明和作者信息保留，各子项目的使用与再分发须遵守原有权利。

见 [迁移说明与验证方法](docs/MIGRATION.md) 和 [验证结果](docs/VALIDATION.md)。

原始仓库现保留于 [只读归档组织](https://github.com/orgs/liujunyukarry-archive/repositories)。完整结果见 [最终验收报告](docs/FINAL_REPORT.md)。
