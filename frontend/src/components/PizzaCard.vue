<template>
  <div id="card_block">
    <div id="left">
      <!-- <img id="PizzaImage" alt="Pizza image" src="../assets/bavarskaya.png" /> -->
      <div id="ImageDiv">
        <img
          id="PizzaImage"
          :alt="pizza.name"
          v-bind:src="'http://127.0.0.1:8000/media/' + pizza.photo"
        />
        <!-- <img v-bind:src="'http://127.0.0.1:8000/media/' + pizza.visual_photo" v-bind:hidden="{  }" /> -->
      </div>
    </div>

    <div id="right">
      <div id="PizzaTitle_div">
        <span id="PizzaTitle_h1">
          {{ pizza.name }}
        </span>
      </div>

      <div id="PizzaInfo_div">
        <span id="PizzaInfo_span">
          {{ pizza.ingredients }}
        </span>
      </div>

      <div id="DownBlock">
        <div id="button" @click="showModal()">
          <button id="Choose">Выбрать</button>
        </div>

        <span id="PizzaPrice"> от {{ pizza.price_small }}₽ </span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ["pizza"],
  methods: {
    showModal: function () {
      this.$emit("show", this.pizza.id_);
    },
  },
};
</script>

<style scoped>

 
#card_block {
  width:  50%;
  height: fit-content;
  box-shadow: 16px 16px 16px #00000040;
  border-radius: 15px;
  background-color: #fff;
  margin: 5px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  flex-wrap: wrap;
}

#right {
  width: 60%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  
}
#PizzaTitle_div {
  height: auto;
  
}

#PizzaTitle_h1 {
  color: #be0000;
  font-family: "Roboto";
  font-weight: 700;
  text-transform: uppercase;
  font-size: 150%;
  display: flex;
  align-self: center;
}

#left {
  width: 40%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
}
#ImageDiv {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

#PizzaImage {
  width: 70%;
  height: auto;
}

#PizzaInfo_div {
  width: 90%;
  height: auto;
}

#PizzaInfo_span {
  color: #000;
  opacity: 64%;
  text-align: left;
  font-family: "Roboto";
  font-weight: 300;
  font-size: 14px;
  line-height: 18px;
  flex-wrap: wrap;
}

#DownBlock {
  width: 90%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
}

#Choose {
  width: 80px;
  height: 35px;
  background-color: #fe310c61;
  border: none;
  box-shadow: 0px 5px 8px #00000040;
  border-radius: 40px;
  color: #be0000;
  font-family: "Roboto";
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
}

#PizzaPrice {
  font-weight: 700;
  font-family: "Roboto";
  font-size: 24px;
}
</style>
