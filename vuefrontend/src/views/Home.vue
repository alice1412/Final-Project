<template>
  <div class="home">
    <NavBar />
    <Content />
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/Navbar-Top/index.vue";
import Content from "@/components/Content/index.vue";

export default {
  name: "Home",
  components: {
    Content,
    NavBar,
  },
};
</script>
