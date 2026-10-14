# Vue 3 后台管理系统学习项目

基于 Vue 3、Vue Router、Vuex、Axios 和 Element Plus 相关依赖的后台管理系统示例。此仓库的实际项目在 **`code/` 子目录**，而非仓库根目录。

## 目录

```text
code/
├── package.json
├── yarn.lock
├── public/
└── src/
    ├── assets/
    ├── components/
    ├── router/
    ├── store/
    ├── util/
    └── views/
```

## 安装与运行

先安装项目实际兼容的 Node.js / Yarn，然后：

```bash
cd code
yarn install
yarn serve
```

构建：`yarn build`；静态检查：`yarn lint`。这些命令源于 `code/package.json` 的实际 scripts；**本次尚未运行测试**，旧依赖和后端 API 可能需要额外配置。

## 维护与安全

- 保持 `code/yarn.lock` 与包管理器一致，避免无意升级依赖导致示例损坏。
- 接入真实后端前检查接口地址、身份认证和演示凭据，不要把真实密钥直接提交到 Git。
- 对目录调整、路由调整和构建工具升级分别做提交，确保问题可以回滚。
- 补充功能前先检查对应 Vue 组件、状态管理与路由，避免与其他 Vue 版本项目混淆。
