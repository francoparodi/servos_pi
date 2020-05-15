function createSlider(sliderId, sliderInputId) {
    var slider = document.getElementById(sliderId);
    var sliderInput = document.getElementById(sliderInputId);
    noUiSlider.create(slider, {
        start: sliderInput.value,
        connect: true,
        step: 2,
        range: {
            'min': 2,
            'max': 12
        },
        tooltips: true,
        pips: {
            mode: 'steps',
            stepped: true,
            density: 4
        }
    });

    slider.noUiSlider.on('update', function (values, handle) {    
        sliderInput.value = values[handle];
    });
}
