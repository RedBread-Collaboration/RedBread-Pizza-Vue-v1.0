<template>
  <div class="Ticket_block">
    <div class="main_block">
      <div class="info_block">
        <div class="line_up">
          <div class="product_id">ID Заказа: {{ ticket.id_ }}</div>
          <div class="user_id">Имя Пользователя: {{ ticket.username }}</div>
          <div class="status">{{ ticket.status }}</div>
        </div>
        <div
          v-for="item in items"
          :key="item.pizza_name"
          :item="item"
          class="order_info"
        >
          <div>
            <div class="Pizza_name">
              <div class="name">
                <span>{{ item.pizza_name }}</span>
              </div>
              <div class="counter">x1</div>
            </div>
            <div class="Pizza_parameters">
              {{ item.pizza_dough }} ; {{ item.pizza_size }} ;
              {{ item.pizza_pieces }} ;
            </div>
          </div>
          <div class="items_additive">
            <div class="additives_span">
              <span>Дополнения:</span>
            </div>
            <div class="additives_items">
              {{ item.pizza_additives }}
            </div>
          </div>
          <div>Цена Позиции: {{ item.price }}₽</div>
          <!-- {{ticket.items}}</div> -->
          <!-- <div class="final_price">Сумма заказа: {{ ticket.final_price }}₽</div> -->
        </div>
        <div class="final_price">Сумма заказа: {{ ticket.final_price }}₽</div>
      </div>
      <div class="admin_buttons">
        <div style="padding-bottom: 10px" id="button_change">
          <button id="Choose" type="button" @click="authorize()">
            Изменить
          </button>
        </div>
        <div id="button_delete">
          <button id="Choose" type="button" @click="authorize()">
            Удалить
          </button>
        </div>
      </div>
    </div>
    <div class="qr_code">
      <img src="http://127.0.0.1:8000/static/qr.png" />
    </div>
  </div>
</template>
<script>
export default {
  props: ["ticket"],
  data() {
    return {
      items: JSON.parse(this.ticket.items),
    };
  },
};
</script>
<style scoped>
.Ticket_block {
  width: 100%;
  height: fit-content;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  border-bottom: 2px solid #000;
  padding: 3% 0%;
}

.main_block {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border: 2px solid grey;
}

.info_block {
  width: 95%;
  font-size: 100%;
  height: fit-content;
  display: flex;
  align-self: center;
  flex-direction: column;
  justify-content: space-between;
}

.line_up {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  font-weight: 700;
  padding-left: 2%;
}

.status {
  display: flex;
  align-self: center;
  font-size: 120%;
  text-decoration: underline;
}

.order_info {
  display: flex;
  flex-direction: column;
  padding-left: 5%;
}

.items {
  display: flex;
  flex-direction: column;
  margin-bottom: 2%;
}

.Pizza_name {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding-right: 70%;
}

.name {
  font-size: 105%;
  font-weight: 600;
}

.Pizza_parameters {
  font-style: italic;
  text-decoration: underline;
}

.items_additive {
  display: flex;
  flex-direction: row;
}

.additives_items {
  font-style: italic;
}

.admin_buttons {
  width: 30%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}

#Choose {
  width: 100%;
  height: 40px;
  background-color: #ff5757;
  border: none;
  border-radius: 40px;
  color: #fff;
  font-family: "Roboto";
  font-size: 100%;
  font-weight: 700;
  cursor: pointer;
}
</style>