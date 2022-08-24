<template>
  <div id="basket_position">
    <div id="right">
      <div id="ImageDiv">
        <img
          id="PizzaImage"
          :alt="cart.name"
          v-bind:src="'http://127.0.0.1:8000/media/' + cart.product.photo"
        />
      </div>
    </div>
    <div id="left">
      <div id="left_up">
        <span id="PizzaTitle">
          {{ cart.product.name }}
        </span>
        <div id="cross_div">
          <button id="cross" @click="show = 0">
            <img
              id="cross"
              :alt="cross"
              @click="delPizza()"
              v-bind:src="'http://127.0.0.1:8000/static/cross.svg'"
            />
          </button>
        </div>
      </div>
      <div id="left_center">
        <span id="pizza_parameters"
          >{{ cart.dough }} {{ cart.size }} + {{ cart.additives }}</span
        >
      </div>
      <div id="left_down">
        <div id="counter">
          <div id="minusDiv">
            <button id="button_count" @click="pizzaMinus()">-</button>
          </div>
          <div>{{ count }}</div>
          <div id="plusDiv">
            <button id="button_count" @click="pizzaPlus()">+</button>
          </div>
        </div>
        <div id="position_price">{{ final_price }}₽</div>
      </div>
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
  props: ["cart"],
  data() {
    return {
      count: this.cart.count,
      final_price: this.cart.final_price,
    };
  },
  methods: {
    delPizza() {
      const delete_cart_item_mutation = gql`
        mutation {
          delete_cart(id_: "${this.cart.id_}")
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

      request(url, delete_cart_item_mutation, null, _headers).then((data) => {
        console.log("Data", data);
        this.count = 0;
        this.final_price = 0;
      });
    },
    pizzaPlus() {
      const update_cart_count_mutation = gql`
        mutation {
          cart_update_count(
            cart: { id_: "${this.cart.id_}", count: ${this.count + 1} }
          ) {
            count
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

      request(url, update_cart_count_mutation, null, _headers).then((data) => {
        console.log("Data", data);
        this.count = data.cart_update_count.count;
        this.final_price = data.cart_update_count.final_price;
      });
    },
    pizzaMinus() {
      if (this.count > 1) {
        const update_cart_count_mutation = gql`
        mutation {
          cart_update_count(
            cart: { id_: "${this.cart.id_}", count: ${this.count - 1} }
          ) {
            count
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

        request(url, update_cart_count_mutation, null, _headers).then(
          (data) => {
            console.log("Data", data);
            this.count = data.cart_update_count.count;
            this.final_price = data.cart_update_count.final_price;
          }
        );
      }
    },
  },
};
</script>
<style scoped>
#basket_position {
  height: 20%;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  border-bottom: 1px solid #00000017;
  padding-right: 5%;
  align-items: center;
}

#right {
  width: 40%;
  display: flex;
  justify-content: center;
  align-content: center;
}
#ImageDiv {
  width: 100%;
  display: flex;
  justify-content: center;
  align-content: center;
}

#PizzaImage {
  width: 50%;
  height: auto;
}

#PizzaTitle {
  font-size: 100%;
  font-weight: 700;
  padding-top: 10%;
}

#left {
  width: 60%;
  height: fit-content;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: stretch;
}
#left_up {
  height: fit-content;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 10px;
}
#left_center {
  height: fit-content;
  padding-bottom: 10px;
}

#counter {
  width: 35%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
#pizza_parameters {
  font-size: 15px;
}

#left_down {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 10px;
}

#button_count {
  width: 20px;
  height: 20px;
  background-color: #fe310c61;
  border: none;
  box-shadow: 0px 5px 8px #00000040;
  border-radius: 40px;
  color: #be0000;
  font-family: "Roboto";
  font-size: 15px;
  font-weight: 700;
}

#cross {
  width: 30px;
  height: auto;
  margin-left: auto;
  margin-right: 5%;
  margin-top: -5%;
  background: none;
  border: none;
  cursor: pointer;
}

#position_price {
  font-weight: 700;
}
</style>
