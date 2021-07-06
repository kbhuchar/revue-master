<template>
  <div>
    <div id="app" class="dropdown">
      <p class="prompt">Select a location:</p>
      <select
        v-model="selectedLocations"
        class="box"
        @change="changeLocation($event.target.value)"
      >
        <option disabled selected>Locations</option>
        <option
          v-for="option in currentService.locations"
          :value="option.name"
          v-bind:key="option"
        >
          {{ option.name }}
        </option>
      </select>
    </div>
    <div>
      <p class="prompt">Rating:</p>
      <select
        v-model="RatingValue"
        class="box"
        @change="changeRating($event.target.value)"
      >
        <option
          v-for="value in ratings"
          :value="value"
          v-bind:key="value in ratings"
        >
          {{ value }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
import store from "@/store/index";
export default {
  name: "Dropdown",
  emits: ["location", "rating"],
  data() {
    return {
      currentService: [],
      selectedLocations: null,
      ratings: [1, 2, 3, 4, 5],
      RatingValue: null,
    };
  },
  mounted() {
    this.currentService = store.state.selectedService;
  },
  methods: {
    changeLocation(event) {
      console.log(event);
      this.$emit("location", event);
    },
    changeRating(event) {
      console.log(event);
      this.$emit("rating", event);
    },
  },
};
</script>
<style scoped>
.box {
  width: 100%;
  position: relative;
  font-size: 25px;
  background: rgb(223, 224, 221);
}
.prompt {
  font-size: 25px;
  text-align: center;
}
.dropdown {
  top: 11px;
  left: 11px;
  font-size: 25px;
}
</style>
