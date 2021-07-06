<template>
  <div class="autocomplete">
    <div class="popover" v-show="visible">
      <input
        type="text"
        v-model="query"
        placeholder="Search for a service..."
      />
      <div class="options">
        <ul>
          <li
            v-for="(match, index) in matches"
            :key="match[filterby]"
            :class="{ selected: selected == index }"
            @click="itemClicked(index)"
            v-text="match[filterby]"
          ></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import ServicesService from '@/services/ServicesService'
export default {
  name: "SearchBox",
  props: ["items", "filterby"],
  data() {
    return {
      selected: 0,
      selectedItem: null,
      query: "",
      visible: true,
      temp: []
    };
  },
  methods: {
    toggleVisible() {
      this.visible = !this.visible;
    },
    itemClicked(index) {
      this.getServiceDetails(index)
      this.selected = index;
      //console.log(this.matches[index]);
    },
    selectItem() {
      this.selectedItem = this.matches[this.selected];
      this.visible = false;
    },
    getServiceDetails(index){
      var serviceName = String(this.matches[index].name);

      ServicesService.getService(serviceName).then(response => {
        this.$store.dispatch('setServiceState', response.data);
        this.$router.push({ name: "service" });
        }).catch(e => {
        this.error = e.response.data
      })
    }
  },
  computed: {
    matches() {
      if (this.query == "") {
        return [];
      }
      return this.items.filter((item) =>
        item[this.filterby].toLowerCase().includes(this.query.toLowerCase())
      );
    },
  },
};
</script>

<style scoped>
.autocomplete {
  width: 100%;
  
  position: relative;
}
.close {
  position: absolute;
  right: 2px;
  top: 4px;
  background: none;
  border: none;
  font-size: 30px;
  color: lightgrey;
  cursor: pointer;
}
.placeholder {
  position: absolute;
  top: 11px;
  left: 11px;
  font-size: 25px;
  color: #d0d0d0;
  pointer-events: none;
}
.popover {
  min-height: 50px;
  min-width: 100%;
  
  border: 2px solid lightgray;
  position: absolute;
  left: 0;
  right: 0;
  background: #fff;
  border-radius: 3px;
  text-align: center;
}
.popover input {
  width: 98%;
  margin-top: 5px;
  height: 40px;
  font-size: 16px;
  border-radius: 3px;
  border: 1px solid lightgray;
  padding-left: 8px;
}
.options {
  max-height: 200px;
  overflow-y: scroll;
  margin-top: 5px;
}
.options ul {
  list-style-type: none;
  text-align: left;
  padding-left: 0;
}
.options ul li {
  border-bottom: 1px solid lightgray;
  padding: 10px;
  cursor: pointer;
  background: #f1f1f1;
}
.options ul li:first-child {
  border-top: 2px solid #d6d6d6;
}
.options ul li:hover {
  background: #8c8c8c;
  color: #fff;
}
</style>
