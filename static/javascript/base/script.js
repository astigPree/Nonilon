let stopAnimation = false;

setInterval( () =>{
    const circles = document.querySelectorAll(".loading-circle");
    let found = false

    for (let i = 0; i < circles.length; i++){
        const item = circles.item(i);
        
        if(found){
            item.classList.add('loading-circle-current');
            break;
        }

        if(item.classList.contains('loading-circle-current')){
            item.classList.remove('loading-circle-current');
            found = true 
        }
    }
    
    if(!found){
        const item = circles.item(0);
        item.classList.add('loading-circle-current'); 
    }

    if (stopAnimation){
        clearInterval();
    }
 

}, 500)

function isElementVisible(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}


function toastAnimation( message ) {
    const toast = document.getElementById('toast');
    const toast_message = document.getElementById('toast-message');
    toast_message.innerText = message;
    
    console.log('toast animation');

    toast.classList.add('popup-toast');
    setTimeout(() => {
        toast.classList.remove('popup-toast');
    }, 6500);
}

// window.addEventListener('unload', function() { 
//     circleAnimations() 
// });

window.addEventListener('load' , function() {
    const loadingPage = document.getElementById('loading-page')
    loadingPage.classList.add('remove-display')
});

