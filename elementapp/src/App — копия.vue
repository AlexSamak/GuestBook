<template>
  <div id="app">
    <div class="app">
      <el-container>

        <el-header>
          <div class="app-header">
            <el-row>              
              <h1>Гостевая книга</h1>              
            </el-row>        
          </div>

          <div class="bnt-space">
            <el-row>              
              <el-button type="primary" class="newEntry" @click="showPopup" > Новый отзыв </el-button>             
            </el-row>         
          </div>
        </el-header>
        

        <el-main>

          <template v-for="item in users">

          <el-row :gutter="10">
            <el-col :span="12">
              <div class="grid-content bg-purple">
                <p>{{item.name}}</p>
                <p>{{item.age}}</p>
                <img src="./assets/vue.jpg">
              </div>
            </el-col>
            <el-col :span="12">
              <div class="grid-content bg-purple">
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet doloribus sit, sunt aspernatur quibusdam. Aperiam illo eius omnis, ducimus qui maiores animi tempora, vel in, doloremque cum distinctio fugit, voluptatem esse dicta impedit id dolorem soluta cumque harum possimus natus commodi illum! Quae eveniet atque veritatis, dolorum consequatur labore eaque.</p>
              </div>
            </el-col>
          </el-row>

        </template>

        <v-popup v-if="IsPopupVisible" @close-event="closeInfoPopup"> <p>Абра кадабра</p> </v-popup>

      </el-main>


        </el-container>  

      </div>           
    </div>
  </template>

  <script>
    import vPopup from './components/popup/v-popup'
    export default {
      name: 'app',
      components: {
        vPopup
      },
      data() {
        return {
          IsPopupVisible: false,
          users: [
                    {name:'Tom', age:22}, 
                    {name:'Bob', age:31}, 
                    {name: 'Sam', age:28}
                  ]
        }
      },
      methods: {
        showPopup(){
          this.IsPopupVisible = true;
          console.log(this.IsPopupVisible);
        },
        closeInfoPopup(){
          this.IsPopupVisible = false;
        }

      }


    }
  </script>

  <style lang="scss">

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  .el-header {
    background-color: #B3C0D1;
    color: #333;
    min-height: 100px;    
  }
  .app-header{
    text-align: center;
    line-height: 10px;
    color: #1F262A;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    min-height: 800px;
  //text-align: center;
  //line-height: 160px;
}

.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }

}
.el-col {
  border-radius: 4px;
}

.bg-purple {
  background: #d3dce6;
}

.grid-content {
  border-radius: 4px;
  margin-top: 15px;
  //min-height: 36px;
  height: 220px;
  text-align: left;
  //color: white;
  //line-height: 10px;
}

</style>
