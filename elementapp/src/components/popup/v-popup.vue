
<template>
  <div class="v-popup">

    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">

      <el-form-item label="Ваше имя" prop="name">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>

      <el-form-item label="Отзыв" prop="comment">
        <el-input type="textarea" v-model="ruleForm.comment"></el-input>
      </el-form-item>

      <el-upload
      class="upload-pict"
      drag
      action="https://jsonplaceholder.typicode.com/posts/"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :file-list="fileList"
      multiple>
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">Перетащите файл или <em>нажмите для выбора</em></div>
      <div class="el-upload__tip" slot="tip">jpg/png файл не более 500kb</div>
    </el-upload>

    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">Отправить</el-button>
      <el-button @click="$emit('close-event')" >Закрыть</el-button>
    </el-form-item>



  </el-form>


</div>
</template>

<script>
export default {
  name: 'v-popup',
  data() {
    return {
      ruleForm: {
        name: '',
        comment: ''
      },
      rules: {
        name: [
        { required: true, message: 'Пожалуйста, укажите свое Имя', trigger: 'blur' },
        { min: 3, max: 32, message: 'Имя длиной от 3 до 32 символов', trigger: 'blur' }
        ],
        comment: [
        { required: true, message: 'Пожалуйста, напишите свой Отзыв', trigger: 'blur' },
        { min: 16, max: 512, message: 'Сообщение длиной от 16 до 512 символов', trigger: 'blur' }
        ]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          //alert('submit!');
          //console.log(this.ruleForm.name);
          //console.log(this.ruleForm.comment);


          const URL = "http://localhost:8000/api/gbooks/";
          var vAttributes = {};
          vAttributes = {
            name: this.ruleForm.name, 
            comment: this.ruleForm.comment
          };
          const ops = {
            method: 'post',
            headers: { 'content-type': 'application/json' },
            data: JSON.stringify(vAttributes) ,
            url: URL
          };
          //console.log(ops.data);
          axios( ops).then((res) => {
            console.log("post response: " + res);
          }).catch(function (error) {
            console.log("post error: " + error);
          });

          this.$emit('close-event');


    } else {
      console.log('error submit!!');
      return false;
    }
  });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
}
</script>

<style lang="scss">
@import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
.v-popup {
  padding: 16px;
  position: fixed;
  top: 150px;
  left: 400px;
  width: 400px;
  min-height: 100px;
  box-shadow: 0 0 17px 0 #e7e7e7;
  opacity: 0.9;
  background-color: #FDFFF5;
  z-index: 10;

  &_header, &_footer{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  &_content{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
}

.submit_btn {
  padding: 8px;
  color: #ffffff;
  background: #26ae68;
} 

.close_modal {
  padding: 8px;
  color: #ffffff;
  background: red;
} 

</style>
