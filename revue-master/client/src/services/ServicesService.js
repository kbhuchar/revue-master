//Yes I'm going with this name
import Api from "@/services/Api";

export default {
  list() {
    return Api().get("services");
  },
  getService(s) {
    return Api().get("services/" + s);
  },
  create(review) {
    return Api().post("addreview", review);
  },
};
