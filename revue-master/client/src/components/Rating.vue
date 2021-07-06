<template>
    <div class="star-rating">
      <ul>
        <li class="visible-stars" v-for="rating in parseInt(value)"  v-bind:key="rating">★</li>
        <li class="invisible-stars" v-for="rating in parseInt(5-value)"  v-bind:key="rating">★</li>
      </ul>
    </div>
</template>
<script>
export default {
  name: 'Rating',
  props: {
    'name': String,
    'value': null,
    'id': String,
    'disabled': Boolean,
    'required': Boolean
  },

  /*
   * Initial state of the component's data.
   */
  data: function() {
    return {
      temp_value: null,
      ratings: [1, 2, 3, 4, 5]
    };
  },

  methods: {
    /*
     * Behaviour of the stars on mouseover.
     */
  }
}

</script>
<style>
.star-rating {
  display: inline-block;
}
.visually-hidden {
  position: absolute;
  overflow: hidden;
  clip: rect(0 0 0 0);
  height: 1px; width: 1px;
  margin: -1px; padding: 0; border: 0;
}



  .invisible-stars {
    display: inline-block;
    padding: 3px;
    vertical-align: middle;
    line-height: 1;
    font-size: 1.5em;
    color: #ABABAB;
    transition: color .2s ease-out;
  }

  .visible-stars {
    display: inline-block;
    padding: 3px;
    vertical-align: middle;
    line-height: 1;
    font-size: 1.5em;
    color: #cac726;
    transition: color .2s ease-out;
  }


</style>
