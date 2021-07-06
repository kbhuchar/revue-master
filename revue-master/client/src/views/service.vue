<template>
  <div class="container">  
  <div class="row">
    <div class="col-sm">
      <img src="/assets/Knox.jpg" class="rounded float-left" width="300px;" height="300px;" >
    </div>
    <div class="col-sm">
      <p>Services</p>
    </div>
    <div class="col-sm">
      <img src="/assets/Knox_oldmain.jpg" width="450px;" height="300px; " />
    </div>
  </div>

<div class="searchbox">
          <SearchBox :items="services" filterby="name" />
          </div>
    <div class="bod">
      
      <h2>{{ currentService.name }}</h2>
      <h4>{{ currentService.description }}</h4>

      <LocationsDisplay></LocationsDisplay>
    </div>

    <div class="student">
      <h5>Student Reviews</h5>
      
      
      <input
        type="button"
        value="Add Reviews"
        style="float: right; font-size:20px;font-weight: bold; ,margin:0 0 0;"
        @click="$router.push({ name: 'create_review' })"
      />
      <span
        class="reviewsTop"
        v-for="location in currentService.locations"
        v-bind:key="location"
      >
        {{ location.name }} <br />
        <ul class="reviewsMiddle">
          <li v-for="Review in location.reviewList" v-bind:key="Review">
            {{ Review.username }} <br />
            {{ Review.title }} <Rating :value=Review.rating></Rating> <br />
            {{ Review.content }} <br /><br />
          </li>
        </ul>
      </span>

      
    </div>
  </div>
</template>

<script>
import SearchBox from "@/components/SearchBox";
import ServicesService from "@/services/ServicesService";
import LocationsDisplay from "@/components/LocationsDisplay";
import Rating from "@/components/Rating";
import store from "@/store/index";
export default {
  name: "Service",
  components: {
    SearchBox,
    LocationsDisplay,
    Rating,
  },
  data() {
    return {
      services: [],
      currentService: [],
    };
  },
  mounted() {
    this.services = this.fetchData();
    this.currentService = store.state.selectedService;
  },
  watch: {
    $route() {
      this.fetchData();
    },
  },
  methods: {
    fetchData() {
      ServicesService.list()
        .then((response) => {
          this.services = response.data;
        })
        .catch((e) => {
          this.error = e.response.data;
        });
    },
  },
};
</script>

<style scoped>



.col-sm{
  font-size: 120px;
  font-weight: bold;
  color:white;
  text-align: center;
}
.searchbox {


  width: 900px;
  margin: auto;
  width: 50%;
 
}

.bod {
  margin: 150px 30px 0;
  font-size: 30px;
  font-weight: bold;
  text-align: left;
  color: darkslategrey;
  color:white;
}

.locate {
  margin: 125px 30px 0;
  font-size: 45px;
  font-weight: bold;
  text-align: left;
  color: darkslategrey;
}
.student {
  margin: 35px 30px 0;
  font-size: 25px;
  font-weight: bold;
  text-align: left;
  color: darkslategrey;
  color:white;
  background-color:black;
}

h2{
  color:white;
}
.h4{
  color:white;
}
h5{
  color:white;
  font-size: 40px;
  font-weight: bold;
}
.container{
  
background-color:rosybrown;
background-image: url('/assets/o.jpg');
background-size:1900px 1150px ;
background-repeat: no-repeat;
min-width:100%;
min-height: 100%;
}
input[type=button]{
  display: inline-block;
  background: linear-gradient(45deg, #87adfe,#ff77cd);
  border-radius:100px;
  padding:10px 20px;
  box-sizing: border-box;
  text-decoration:seashell;
  color: #fff;
  box-shadow: 3px 8px 22px rgba(94,28,68,0.15);
   text-shadow: 0 1px 1px rgba(207, 35, 35, 0.2);

}
input[type=button]:hover{
  background:turquoise;
  
}


</style>
