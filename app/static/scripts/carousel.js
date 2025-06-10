document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('carousel');
    const items = carousel.children;
    const itemCount = items.length;
    const itemWidth = items[0].offsetWidth + 16; // 16px for gap
    const nextBtn = document.getElementById('nextBtn');
    const prevBtn = document.getElementById('prevBtn');
    const scrollIndicators = document.getElementById('scrollIndicators');
    
    scrollIndicators.scrollBy({left: 122, behavior: 'instant'});

    if (nextBtn && carousel) {
        nextBtn.addEventListener('click', () => {
          nextFTrain();
    });
    }

    if (prevBtn && carousel) {
        prevBtn.addEventListener('click', () => {
          prevFTrain();
        });
    }

    var nextFTrain = function(){
      if(carousel.scrollLeft >= itemWidth * (itemCount - 1)){
          carousel.scrollLeft = 0;
          scrollIndicators.scrollBy({left: 104, behavior: 'instant'});
          cooldown(nextBtn);
      }
      else{
          carousel.scrollBy({ left: itemWidth, behavior: 'smooth' });
          scrollIndicators.scrollBy({left: -26, behavior: 'instant'});
          cooldown(nextBtn);
      }
    }

    var prevFTrain = function() {
      if (carousel.scrollLeft < itemWidth){
        console.log(carousel.scrollLeft);
        carousel.scrollLeft = itemWidth * 4;
        scrollIndicators.scrollBy({left: -104, behavior: 'instant'});
        cooldown(prevBtn);
          }
      else {
        carousel.scrollBy({ left: -itemWidth, behavior: 'smooth' });
        scrollIndicators.scrollBy({left: 26, behavior: 'instant'});
        cooldown(prevBtn);
      } 
    }
});
    //cooldown function
    var cooldown = function(x){
      x.disabled = true;
      console.log("on cooldown")
      setTimeout(() => {
        console.log("not cooldown")
        x.disabled = false;
      }, 600);
    }


    

