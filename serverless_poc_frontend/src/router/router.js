import Vue from "vue";
import Router from "vue-router";

export const routers = [
    {
        path: "/",
        name: "list-scripts",
        component: () =>
            import(/* webpackChunkName: "ListPage" */ "@/components/ListScripts"),
    },
    {
        path: "/script/add",
        name: "add-script",
        component: () =>
            import(/* webpackChunkName: "ListPage" */ "@/components/AddScript"),
    },
    {
        path: "/script/execute/:scriptName",
        name: "execute-script",
        component: () =>
            import(/* webpackChunkName: "ListPage" */ "@/components/ExecuteScript"),
    }
];

Vue.use(Router);
const RouterConfig = {
    mode: "history",
    routes: routers
};

export const router = new Router(RouterConfig);