# Vue 2 / Vue 3 / TypeScript 后台项目对照资料

本仓库是包含多种 Vue 技术栈的**学习与对照工程集合**，不是单一 Vue App。原有中文资料目录和三套工程源码保持不变。

## 项目目录

```text
Vue_project/
├── 1项目效果展示/                 # 效果截图
├── 2Vue多版本及cli切换/           # 版本切换资料
├── 4vue+ts项目重构文档/           # TypeScript 重构说明
├── 佳楠通用项目接口文档/          # API 资料
└── 项目vue2+ts+vue3源码/
    ├── project-v2/              # Vue 2 工程
    ├── project-v3/              # Vue 3 工程
    └── project-ts/              # Vue 2 + TypeScript 工程
```

## 启动单个工程

**必须先进入具体项目目录**，在那里安装依赖和运行命令；不要在仓库根目录直接运行 `yarn serve`。

```bash
cd "Vue_project/项目vue2+ts+vue3源码/project-v3"
yarn install
yarn serve
```

其它两套工程按需要将 `project-v3` 替换成 `project-v2` 或 `project-ts`。各工程有自己的 `package.json` 与锁文件，应独立安装和构建。

## 工程维护注意事项

- 旧版本依赖可能需要相应 Node.js 版本；实际兼容性尚未验证，勿直接声称在最新 Node.js 上可运行。
- 保留三套工程的独立依赖文件，不能因为目录相似就合并 `src/` 或 `package.json`。
- 学习资料内可能出现演示账号、公开示例地址或本地机器路径；复制到真实生产环境前必须审核并替换。
- 先确保各工程依次可安装、运行、打包，再考虑统一代码风格和重构。
