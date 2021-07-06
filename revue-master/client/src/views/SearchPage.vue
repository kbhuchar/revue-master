<template>
    <div class="SearchPage">
        <h1>Knox Rate-A-Service</h1>
        <SearchBox :items="services" filterby="name" />

    </div>
</template>

<script>
import SearchBox from '@/components/SearchBox'
import ServicesService from '@/services/ServicesService'

//import services from '@/assets/services.js'
export default {
    name: 'Search-Page',
    data(){
        return {
            services: []
        };
    },
    components: { 
      SearchBox
    },
    mounted(){
       this.fetchData()
    },
    watch: {
        $route() {
            this.fetchData()
        }
    },
    methods: {
    fetchData() {
      ServicesService.list()
        .then(response => {
          this.services = response.data
        })
        .catch(e => {
          this.error = e.response.data
        })
    }
  },
}

</script>

<style scoped>
.SearchPage {
  margin: 0px auto;
  margin-top: 60px;
  width: 800px;
}
</style>