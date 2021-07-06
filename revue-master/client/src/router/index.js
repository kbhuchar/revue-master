import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home";

// GUIDE: This file defines urls for the frontend
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/Search",
    name: "Search-Page",
    component: () => import("@/views/SearchPage"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import(/* webpackChunkName: "login" */ "@/views/Login"),
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import(/* webpackChunkName: "signup" */ "@/views/SignUp"),
  },
  {
    path: "/s/:name",
    name: "Subvue",
    component: () => import(/* webpackChunkName: "subvue" */ "@/views/Subvue"),
  },
  {
    path: "/s/:subvuePermalink/:id",
    name: "Post",
    component: () => import(/* webpackChunkName: "post" */ "@/views/Post"),
  },
  {
    path: "/u/:username",
    name: "User",
    component: () => import(/* webpackChunkName: "user" */ "@/views/User"),
  },
  {
    path: "/create",
    name: "CreatePost",
    component: () =>
      import(/* webpackChunkName: "create" */ "@/views/CreatePost"),
  },
  {
    path: "/create/subvue",
    name: "CreateSubvue",
    component: () =>
      import(/* webpackChunkName: "createsubvue" */ "@/views/CreateSubvue"),
  },
  {
    path: "/service",
    name: "service",
    component: () =>
      import(/* webpackChunkName: "services" */ "@/views/service"),
  },
  {
    path: "/Confirmation",
    name: "Confirmation",
    component: () =>
      import(/*webpackChunkName: "Confirmation" */ "@/views/Confirmation"),
  },
  {
    path: "/Dropdown",
    name: "DropDown",
    component: () => import("@/components/ReviewDropdown"),
  },
  {
    path: "/addreview",
    name: "create_review",
    component: () => import("@/views/CreateReview"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
