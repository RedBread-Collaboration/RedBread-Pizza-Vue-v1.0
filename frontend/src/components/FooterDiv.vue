<template>
  <div class="footer">
    <div class="authors">
      <div class="copyright">
        <span class="copyright_span">RedBread Pizza © 2022</span>
      </div>
      <div class="callback_block">
        <div class="callback_span">
          <span class="span">Обратная связь:</span>
        </div>
        <div class="telegram_block">
          <div class="telegram_tag">
            <img class="telegram_icon" src="http://127.0.0.1:8000/static/telegram.png" />
            <span>
              <a href="https://t.me/IT_KittyK">@IT_KittyK</a>
            </span>
          </div>
          <div class="telegram_tag">
            <img class="telegram_icon" src="http://127.0.0.1:8000/static/telegram.png" />
            <span>
              <a href="https://t.me/HaroldBlakk">@HaroldBlakk</a>
            </span>
          </div>
          <div class="telegram_tag">
            <img class="telegram_icon" src="http://127.0.0.1:8000/static/telegram.png" />
            <span>
              <a href="https://t.me/Parzivalll">@Parzivalll</a>
            </span>
          </div>
          <div class="telegram_tag">
            <img class="telegram_icon" src="http://127.0.0.1:8000/static/telegram.png" />
            <span>
              <a href="https://t.me/syrnnik">@syrnnik</a>
            </span>
          </div>
        </div>
      </div>

      <div class="see_soon">
        <span>Скоро появимся в:</span>
        <div class="icon_block">
          <div>
            <img class="soon_icon" src="http://127.0.0.1:8000/static/vk.png" />
          </div>
          <div>
            <img class="soon_icon" src="http://127.0.0.1:8000/static/whatsapp.png" />
          </div>
        </div>
      </div>
    </div>

    <div class="footer_logo">
      <img src="http://127.0.0.1:8000/static/header_logo.png" />
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.footer {
  background-color: #ff5757;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  height: fit-content;
  width: 100%;
  color: #fff;
  font-weight: 700;
}

.callback_block {
  width: 60%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-wrap: wrap;
  text-align: center;
}
.callblack_span {
  width: 30%;
  display: flex;  

}

.span{
  font-size: 20px;
}
.telegram_block {
  height: fit-content;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
}

.telegram_tag {
  display: flex;
  font-weight: lighter;
  margin-left: 20px;
  flex-wrap: wrap;
  height: fit-content;
}

.telegram_tag span {
  display: flex;
  align-self: center;
  font-size: 20px;
}

.telegram_icon {
  height: 20px;
  width: 20px;
  align-self: center;
}

.authors {
  width: 85%;
  height: fit-content;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  margin-left: 3%;
}

.copyright {
  padding-bottom: 1%;
  display: flex;
  font-weight: lighter;
  font-size: 100%;
  height: 90px;
  align-items: flex-end
}

.see_soon {
  height: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-left: auto;
  flex-wrap: wrap;
  text-align: center;
  font-size: 15px;
}

.see_soon div {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  height: fit-content;
}
.icon_block {
  width: 30%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  flex-wrap: wrap;
  height: fit-content;
}

.soon_icon {
  height: 30px;
  width: 30px;
  align-self: center;
}

.footer_logo {
  width: 10%;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-self: center;
  flex-wrap: wrap;
}

.footer_logo img {
  height: 90px;
}
</style>