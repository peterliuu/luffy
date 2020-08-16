<template>
  <el-carousel height="720px" :interval="3000" arrow="always">
    <el-carousel-item v-for="item in imgList" :key="item">
      <img :src="item" alt="" width="100%">
    </el-carousel-item>
  </el-carousel>
</template>

<script>
  export default {
    name: "Banner",
    data() {
      return {
        imgList: [
          '/static/image/alex.jpeg',
          '/static/image/banner1.png',
          '/static/image/banner2.png'
        ]
      }
    }
  }
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
