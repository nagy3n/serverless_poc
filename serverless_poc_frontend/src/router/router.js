import Vue from "vue";
import Router from "vue-router";

export const routers = [
    {
        path: "/",
        component: () =>
            import(/* webpackChunkName: "ListPage" */ "@/components/ListScripts"),
    },
    {
        path: "/script/add",
        component: () =>
            import(/* webpackChunkName: "ListPage" */ "@/components/AddScript"),
    },
    {
        path: "/script/execute/:scriptName",
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