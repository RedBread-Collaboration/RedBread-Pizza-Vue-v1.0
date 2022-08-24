<template>
  <div id="ingridients_block" v-if="showModal == pizza.id_">
    <div id="head">
      <div id="PizzaTitle_div">
        <h1 id="PizzaTitle_h1">
          {{ pizza.name }}
        </h1>
        <button id="cross">
          <img
            id="cross"
            :alt="cross"
            v-bind:src="'http://127.0.0.1:8000/static/cross.svg'"
            @click="hideModal()"
          />
        </button>
      </div>
    </div>
    <div id="center_block">
      <div id="left">
        <div class="pieces"></div>
        <img
          id="PizzaImage"
          :alt="pizza.name"
          v-bind:src="'http://127.0.0.1:8000/media/' + pizza.photo"
        />
      </div>
      <div id="right">
        <div id="PizzaInfo_div">
          <span id="PizzaInfo_span">
            {{ pizza.ingredients }}
          </span>
        </div>
        <div id="choose_size">
          <div>
            <button
              class="pizza_size"
              @click="changeSize(0, pizza.price_small)"
              v-bind:class="{ size_color: sizeType == 0 }"
            >
              <span>Маленькая (25 см.)</span>
            </button>
          </div>
          <div>
            <button
              class="pizza_size"
              @click="changeSize(1, pizza.price_medium)"
              v-bind:class="{ size_color: sizeType == 1 }"
            >
              <span>Средняя (30 см.)</span>
            </button>
          </div>
          <div>
            <button
              class="pizza_size"
              @click="changeSize(2, pizza.price_large)"
              v-bind:class="{ size_color: sizeType == 2 }"
            >
              <span>Большая (35 см.)</span>
            </button>
          </div>
        </div>
        <div id="choose_dough">
          <div class="dough_container">
            <button
              class="pizza_size"
              @click="doughType = 0"
              v-bind:class="{ size_color: doughType == 0 }"
            >
              Традиционное
            </button>
          </div>
          <div class="dough_container">
            <button
              class="pizza_size"
              @click="doughType = 1"
              v-bind:class="{ size_color: doughType == 1 }"
            >
              Тонкое
            </button>
          </div>
        </div>
        <div id="choose_size">
          <div>
            <button
              class="pizza_size"
              @click="selectPieces(0)"
              v-bind:class="{ size_color: piecesType == 0 }"
            >
              <span>4 кусочка</span>
            </button>
          </div>
          <div>
            <button
              class="pizza_size"
              @click="selectPieces(1)"
              v-bind:class="{ size_color: piecesType == 1 }"
            >
              <span>6 кусочков</span>
            </button>
          </div>
          <div>
            <button
              class="pizza_size"
              @click="selectPieces(2)"
              v-bind:class="{ size_color: piecesType == 2 }"
            >
              <span>8 кусочков</span>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div id="additive">
      <button
        id="ingridient"
        v-for="additive in additives"
        v-bind:key="additive.id_"
        @click="isActive(additive)"
        v-bind:class="{
          'ingridient-active': this.actives.includes(additive.name),
        }"
      >
        <div>
          <div id="ingridient_img">
            <img
              :alt="additive.name"
              v-bind:src="'http://127.0.0.1:8000/media/' + additive.photo"
            />
          </div>
          <div id="ingridient_name">
            <span>{{ additive.name }}</span>
          </div>
          <div id="ingridient_price">
            <span>{{ additive.price }}₽</span>
          </div>
        </div>
      </button>
    </div>

    <div id="DownBlock" @click="addToCart()">
      <div id="Choose">Добавить в корзину</div>

      <span id="PizzaPrice">{{ totalPrice }}₽ </span>
    </div>
  </div>
</template>
<script>
import { request, gql } from "graphql-request";
import { v4 as uuid4 } from "uuid";
import cookies from "vue-cookies";

var _token = cookies.get("_token");
var _session_id = cookies.get("_Session_ID");

if (_token) {
  console.log("Token found in cookie: ", _token);
} else {
  _token = "";
}

if (_session_id) {
  console.log("Session_ID found in cookie: ", _session_id);
} else {
  _session_id = uuid4();
  cookies.set("_Session_ID", _session_id, "1h");
}

var url = "http://127.0.0.1:8000/graphql";

export default {
  props: ["pizza", "showModal"],
  data() {
    return {
      sizeType: 0,
      doughType: 0,
      piecesType: -1,
      additives: this.getAdditives(),
      actives: [],
      totalPrice: this.pizza.price_small,
      additives_string: "",
    };
  },
  methods: {
    getAdditives: function () {
      const additive_query = gql`
        query {
          additive {
            id_
            name
            photo
            price
          }
        }
      `;
      request(url, additive_query).then((data) => {
        this.additives = data.additive;
        return data.additive;
      });
    },
    hideModal: function () {
      this.$emit("show", 0);
    },
    selectPieces: function (newPieceType) {
      if (this.piecesType == newPieceType) {
        this.piecesType = -1;
      } else {
        this.piecesType = newPieceType;
      }
    },
    getPrice: function () {
      var size = "";
      var dough = "";
      var pieces = "";

      if (!this.sizeType) {
        this.sizeType = 0;
      }

      if (!this.doughType) {
        this.doughType = 0;
      }

      if (!this.piecesType) {
        this.piecesType = -1;
      }

      if (!this.actives) {
        this.actives = [];
      }

      if (this.sizeType == 0) {
        size = "small";
      } else if (this.sizeType == 1) {
        size = "medium";
      } else {
        size = "large";
      }

      if (this.doughType == 0) {
        dough = "traditional";
      } else {
        dough = "thin";
      }

      if (this.piecesType == -1) {
        pieces = "one";
      } else if (this.piecesType == 0) {
        pieces = "four";
      } else if (this.piecesType == 1) {
        pieces = "six";
      } else {
        pieces = "eight";
      }

      var additive_elements = "";
      for (var i = 0; i < this.actives.length; i++) {
        if (i == this.actives.length - 1) {
          additive_elements = additive_elements + this.actives[i];
        } else {
          additive_elements = additive_elements + this.actives[i] + ", ";
        }
      }

      this.additives_string = additive_elements;

      const calculate_price_mutation = gql`mutation {calculate_price(cart: {product_id: "${this.pizza.id_}", count: 1, dough: ${dough}, size: ${size}, pieces: ${pieces}, additives: "${additive_elements}"})}`;
      request(url, calculate_price_mutation).then((data) => {
        this.totalPrice = data.calculate_price;
        console.log(data.calculate_price);
      });
    },
    changeSize: function (type, price) {
      if (this.sizeType == 0)
        this.totalPrice = this.totalPrice - this.pizza.price_small + price;
      else if (this.sizeType == 1)
        this.totalPrice = this.totalPrice - this.pizza.price_medium + price;
      else if (this.sizeType == 2)
        this.totalPrice = this.totalPrice - this.pizza.price_large + price;
      this.sizeType = type;
      this.getPrice();
    },
    isActive: function (additive) {
      var i;

      if (this.actives.includes(additive.name)) {
        i = this.actives.indexOf(additive.name);
        this.actives.splice(i, 1);
        this.getPrice();
      } else {
        this.actives.push(additive.name);
        this.getPrice();
      }
      this.$emit("activeAdditives", this.actives);
    },
    addToCart: function () {
      var size = "";
      var dough = "";
      var pieces = "";
      if (this.sizeType == 0) {
        size = "small";
      } else if (this.sizeType == 1) {
        size = "medium";
      } else {
        size = "large";
      }

      if (this.doughType == 0) {
        dough = "traditional";
      } else {
        dough = "thin";
      }

      if (!this.additives_string) {
        this.additives_string = "";
      }

      if (this.piecesType == -1) {
        pieces = "one";
      } else if (this.piecesType == 0) {
        pieces = "four";
      } else if (this.piecesType == 1) {
        pieces = "six";
      } else {
        pieces = "eight";
      }

      const add_to_cart_mutation = gql`
        mutation {
          cart(
            cart: {
              product_id: "${this.pizza.id_}"
              count: 1
              dough: ${dough}
              size: ${size}
              pieces: ${pieces}
              additives: "${this.additives_string}"
            }
          ) {
            id_
            final_price
          }
        }
      `;

      var _headers = {};

      if (_token) {
        _headers = {
          Authorization: `Bearer ${_token}`,
          Session_ID: _session_id,
        };
      } else {
        _headers = {
          Session_ID: _session_id,
        };
      }

      console.log("Headers", _headers);

      request(url, add_to_cart_mutation, null, _headers).then((data) => {
        console.log("Data", data);
      });

      this.hideModal();
    },
  },
};
</script>

<style scoped>
#ingridients_block {
  width: 50%;
  height: fit-content;
  box-shadow: 16px 16px 16px #00000040;
  border-radius: 15px;
  background-color: #fff;
  margin: 5px;
  display: flex;
  flex-direction: column;
  align-self: center;
  position: absolute;
  top: 20%;
  right: 24%;
}

#cross {
  width: 30px;
  margin-left: auto;
  margin-right: 15px;
  margin-top: 5px;
  background: none;
  border: none;
  cursor: pointer;
}

#PizzaTitle_div {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

#PizzaTitle_h1 {
  width: fit-content;
  color: #000;
  font-family: "Roboto";
  font-weight: 700;
  text-transform: none;
  font-size: 24px;
  margin: 0;
  margin-left: auto;
  margin-top: 15px;
}
#choose_size {
  width: 90%;
  height: fit-content;
  background-color: grey;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 10%;
  background: linear-gradient(
    90deg,
    #0000000a 0%,
    #00000033 47.92%,
    #0000000a 100%
  );
  border-radius: 15px;
}

.pizza_size {
  font-size: 70%;
  width: 100%;
  height: 25px;
  border-radius: 15px;
  border: none;
  background: none;
  cursor: pointer;
  font-weight: 500;
  outline: none;
}

.size_color {
  background: #fff;
}

#choose_dough {
  width: 90%;
  height: fit-content;
  background-color: grey;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 5%;
  background: linear-gradient(
    90deg,
    #0000000a 0%,
    #00000033 47.92%,
    #0000000a 100%
  );
  border-radius: 15px;
}

#pizza_dough {
  font-size: 70%;
  height: 25px;
  width: 100%;
  border-radius: 15px;
  border: none;
  background: none;
  cursor: pointer;
  font-weight: 500;
}

#center_block {
  width: 100%;
  height: fit-content;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

#left {
  width: 50%;
  height: fit-content;
  display: flex;
  justify-content: center;
  align-content: center;
}

#right {
  width: 50%;
  height: fit-content;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-wrap: wrap;
}

#PizzaImage {
  max-width: 100%;
  height: fit-content;
  display: flex;
  flex-direction: column;
  align-self: middle;
}

#PizzaInfo_div {
  width: 90%;
  height: fit-content;
  margin-bottom: 10%;
}

#PizzaInfo_span {
  color: #000;
  opacity: 64%;
  text-align: left;
  font-family: "Roboto";
  font-weight: 300;
  font-size: 80%;
  line-height: 5px;
}
#additive {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
  align-items: center;
}

#DownBlock {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}
#ingridient {
  height: fit-content;
  border: none;
  background: #ffffff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  margin-bottom: 5%;
  cursor: pointer;
}
#ingridient_img {
  margin-top: 10%;
}

#ingridient_name {
  text-align: center;
  margin: 5% 2%;
  font-size: 100%;
  font-weight: 600;
}

#ingridient_price {
  margin-bottom: 5%;
  font-weight: 600;
}

.ingridient-active {
  border: 2px solid #ffa08c !important;
  background: url("http://127.0.0.1:8000/static/checked.png") no-repeat !important;
  background-position: 95% 2% !important;
}

#Choose {
  width: 40%;
  height: 35px;
  background-color: #ff5757;
  border: none;
  box-shadow: 0px 5px 8px #00000040;
  border-radius: 40px;
  color: #fff;
  font-family: "Roboto";
  font-size: 100%;
  font-weight: 700;
  margin-bottom: 2%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  text-align: center;
  cursor: pointer;
}

#PizzaPrice {
  font-weight: 700;
  font-family: "Roboto";
  font-size: 24px;
  align-items: center;
}
</style>