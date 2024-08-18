const menu_button = document.querySelector(".menu");
const banner = document.querySelector(".banner");
const body = document.querySelector("body")

const on_menu_click = (e) => {
    console.log()
    if ("menu-card" == banner.classList[1]) {

        console.log("menu-card state click", menu_button.innerText);
        banner.classList = "banner";
        menu_button.classList = "menu";
        menu_button.innerText = "☰";
        body.style = "overflow:visible;";


    } else {
        console.log("banner state click");
        banner.classList += " menu-card ";
        menu_button.classList += " menu-clicked ";
        menu_button.innerText = "X";
        body.style = "overflow:hidden;";
    }
}

menu_button.addEventListener("click", (e) => on_menu_click(e));

