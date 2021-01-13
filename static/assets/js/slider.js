$('.slider').slick({
    centerMode: true,
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows:true,
    focusOnSelect: true,
    asNavFor: '.slider-for',
});
    
 $('.slider-for').slick({
    centerMode: true,
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider'
});