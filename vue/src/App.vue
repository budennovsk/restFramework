<template>
  <div class="v-klnode"></div>
  <div id="app">
    <vNode />
    <formCreate/>
  </div>
</template>

<script>
import vNode from './components/v-node.vue';
import formCreate from './components/formCreate.vue';



export default {
  name: 'App',
  components: {
    vNode,
    formCreate,
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>


