new Vue({
  el: '#new_comment',
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
          alert('submit!');
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

})
















