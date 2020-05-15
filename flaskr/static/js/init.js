function createSlider(sliderId, sliderInputId) {
    var slider = document.getElementById(sliderId);
    var sliderInput = document.getElementById(sliderInputId);
    noUiSlider.create(slider, {
        start: sliderInput.value,
        connect: true,
        step: 36,
        range: {
            'min': 0,
            'max': 180
        },
        tooltips: true
    });

    slider.noUiSlider.on('update', function (values, handle) {    
        sliderInput.value = values[handle];
    });
}
