let toggleNavStatus = false;
let toggleMobChapters = false;
let toggleSignUp = false;

function hamburgerAnimation(x) {
    x.classList.toggle("change");
    toggleMobNav();
}

function toggleMobNav() {
    let getSideBar = document.querySelector(".navbar");
    let getSideBarUl = document.querySelector(".navbar ul");
    let getSideBarLinks = document.querySelectorAll(".navbar ul li a");

    if (toggleNavStatus == false) {
        getSideBar.style.zIndex = "40";
        getSideBarUl.style.visibility = "visible";
        getSideBar.style.width = "33%";
        getSideBar.style.minwidth = "100px";

        for (let i = 0; i < getSideBarLinks.length; i++) {
            getSideBarLinks[i].style.opacity = "1";
        }

        toggleNavStatus = true;
    }

    else if (toggleNavStatus == true) {
        getSideBar.style.width = "0";
        getSideBarUl.style.visibility = "hidden";
        for (let i = 0; i < getSideBarLinks.length; i++) {
            getSideBarLinks[i].style.opacity = "0";
        }
        toggleNavStatus = false;
    }
}
