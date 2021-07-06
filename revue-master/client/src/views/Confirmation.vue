<template lang="html">
  <div class="confirmation_page">
    <img
      class="confirm_icon"
      alt="confirm icon is here"
      src="@/assets/Verification.jpg"
    />
    <div class="announce">
      <p>
        Thank you for signing up please check your email address to verify your
        account.
      </p>
    </div>
  </div>
</template>

<script>
import AuthenticationService from "@/services/AuthenticationService";
export default {
  name: "Confirmation",

  mounted() {
    AuthenticationService.confirmation();
  },
};
</script>
<style scoped lang="css">
.confirm_icon {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 200px;
}

.announce {
  width: 50%;
  margin: auto;
  text-align: center;
  border: 3px solid rgb(23, 92, 93);
  border-radius: 20px;
}
</style>
