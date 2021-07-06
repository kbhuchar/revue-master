import Api from "@/services/Api";

export default {
  signup(credentials) {
    // GUIDE: An api call. This function takes an argument, credentials, and tries to sign up with it on the server
    return Api().post("signup", credentials);
  },

  login(credentials) {
    return Api().post("login", credentials);
  },

  confirmation() {
    return Api().get("confirmation");
  },
};
