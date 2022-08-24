<template>
  <div class="Cart" v-if="showModal == 'cart'">
    <div id="modal-window">
      <div id="head_basket">
        <div id="basket_logo">
          <img
            id="logo_img"
            src="http://127.0.0.1:8000/static/busket_logo.png"
          />
        </div>
        <div id="headerName">
          <span id="basketName">Корзина</span>
          <span id="counter">{{ cart_size }}</span>
        </div>
        <button id="cross" @click="hideModal()">
          <img id="cross" src="http://127.0.0.1:8000/static/cross.svg" />
        </button>
      </div>
      <BasketPosition
        v-for="cart in carts"
        v-bind:key="cart.id_"
        v-bind:cart="cart"
      />

      <div id="sum">
        <div>
          <span id="order_sum">Сумма заказа:</span>
        </div>
        <div>
          <span id="total_sum">{{ totalPrice }}₽</span>
        </div>
      </div>
      <div id="input_info">
          <label class="label" for="street"> Адрес </label>
          <input
            class="input"
            type="text"
            id="_address"
          />
      </div>
      <div
        id="form"
        @click="
          showModalWin();
          getUserCart();
        "
      >
        <button id="Choose" @click="makeTicket()"><span>Оформить</span></button>
      </div>
    </div>
    <div class="overlay"></div>
  </div>
</template>
<script>
import BasketPosition from "@/components/BasketPosition";

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
  props: ["showModal"],
  components: {
    BasketPosition,
  },
  data() {
    return {
      carts: this.getUserCart(),
      totalPrice: 0,
      cart_size: this.cart_size,
    };
  },
  methods: {
    makeTicket: function () {
      const ticket_mutation = gql`
        mutation {
          ticket(ticket: { address: "" }) {
            id_
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

      request(url, ticket_mutation, null, _headers).then((data) => {
        console.log(data);
        // for (var i = 0; i < this.carts.length; i++) {
        //   this.cart_size = this.cart_size + data.cart[i].count;
        //   this.cart_price = this.cart_price + data.cart[i].final_price;
        // }
      });
    },
    getUserCart: function () {
      const cart_query = gql`
        query {
          cart {
            additives
            count
            final_price
            id_
            dough
            size
            product {
              id_
              ingredients
              name
              photo
            }
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

      var cart_size = 0;
      var cart_price = 0;

      request(url, cart_query, null, _headers).then((data) => {
        this.carts = data.cart;
        for (var i = 0; i < data.cart.length; i++) {
          cart_size = cart_size + data.cart[i].count;
          cart_price = cart_price + data.cart[i].final_price;
        }
        this.cart_size = cart_size;
        this.totalPrice = cart_price;
      });
    },
    showModalWin: function () {
      this.$emit("show", "ticket");
    },
    hideModal: function () {
      this.$emit("show", 0);
    },
  },
};
</script>

<style scoped>
::-webkit-scrollbar {
  width: 0px; /* ширина для вертикального скролла */
  background-color: #7d3131;
}

.Cart {
  position: fixed;
  display: flex;
  flex-direction: column;
  z-index: 100;
  width: 45%;
  height: 100%;
  background-color: #fff;
  top: 0%;
  align-items: center;
  border-radius: 15px;
  overflow: auto;
  background-color: #000000b3;
  justify-content: center;
  align-items: center;
}

#modal-window {
  width: 100%;
  height: 100%;
  z-index: 2;
  background-color: #fff;
  border-radius: 15px;
}
.overlay {
  position: absolute;
  width: 20%;
  height: 100%;
  z-index: 1;
}
#head_basket {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding-top: 5%;
  padding-left: 5%;
  margin-bottom: 5%;
}
.basket_logo {
  width: 30%;
}

#logo_img {
  width: 90%;
  height: auto;
}

#headerName {
  width: 55%;
  font-size: 150%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  flex-wrap: wrap;
}

#basketName {
  font-size: 120%;
  font-weight: 700;
}

#counter {
  font-size: 100%;
  font-weight: 700;
}

#cross {
  width: 30px;
  margin-left: auto;
  margin-right: 5%;
  margin-top: -5%;
  background: none;
  border: none;
  cursor: pointer;
}

#sum {
  margin-top: 5%;
  margin-bottom: 5%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  font-size: 100%;
  font-weight: 700;
  padding: 0% 2%;
}
#form {
  display: flex;
  align-self: center;
  justify-content: center;
  width: 100%;
  margin-bottom: 5%;
}
#Choose {
  width: 70%;
  padding: 2%;
  height: fit-content;
  background-color: #ff5757;
  border: none;
  box-shadow: 0px 5px 8px #00000040;
  border-radius: 40px;
  color: #fff;
  font-family: "Roboto";
  font-size: 100%;
  font-weight: 700;
  cursor: pointer;
}
</style>
