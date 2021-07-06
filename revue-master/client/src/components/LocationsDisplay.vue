<template>
    <div class="list">
      <ul class="locList">
        <li  v-for="location in currentService.locations" v-bind:key="location">
          {{location.name}} <Rating class="rating" :value=avgRating(location)></Rating>
        </li>
      </ul>
    </div>
</template>
<script>
import store from '@/store/index'
import Rating from '@/components/Rating'

export default {
  name: 'LocationsDisplay',
  components: {Rating},
  /*
   * Initial state of the component's data.
   */
  data: function() {
    return {
      currentService: [],
      addedRatings: 0,
    };
  },
  mounted(){
    this.currentService = store.state.selectedService;
    console.log(this.currentService);
  },
  methods: {
    avgRating(locationL){
      var y;
      this.addedRatings = 0;
        var temp = locationL;
        for (y = 0; y < temp.reviewList.length; y++){
          this.addedRatings += temp.reviewList[y].rating;
        }
      if (temp.reviewList.length > 0){
      return this.addedRatings / temp.reviewList.length;
      }
      else {
        return 0;
      }
    },
  }
}
</script>

<style scoped>
.list {
  display: flex;
}

.locList {
  flex: 1;
  margin-top: 20px;
  margin-left: 20px;
}
.rating {
  flex: 3;
}
</style>
