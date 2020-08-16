new Vue({
	//import vPopup from '/static/components/popup/v-popup.vue'
	el: '#book_app',
	
	// components: {
 //      vPopup
 //    },
	data: {
		IsPopupVisible: false,
        comments: [] 
	},
	
	methods: {
		showPopup(){
        this.IsPopupVisible = true;
        console.log(this.IsPopupVisible);
      },
      closeInfoPopup(){
        this.IsPopupVisible = false;
      },
      fetchOrders() {
      	const vm = this;
        axios.get('http://localhost:8000/api/gbooks')
        .then((responce) => {
          const data = responce.data;
          vm.comments = data
      })
     },
	},

	created: function() {
		console.log('Created!');
		this.fetchOrders();
		//this.addData();

	}


}
)

