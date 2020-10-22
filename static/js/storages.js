let pockets = new Map()
let priceholders = new Map()
let plasticholders = new Map()
let pricepapers = new Map()
let others = new Map()

let data = new Map([
    ["pockets", pockets],
    ["priceholders", priceholders],
    ["plasticholders", plasticholders],
    ["pricepapers", pricepapers],
    ["others", others]
]);


/*Pockets section slide and add to virtual cart*/
$(".pocket").click(function () {
    $(".pockets").slideToggle("fast");
});

$(".pockets").find(".button").click(function () {
    let quantity = $(".pocket_module").find(`input[form=${this.id}]`).val();
    if (quantity === "") {
        quantity = 0
    }
    if (pockets.has(+this.id)) {
        pockets.set(+this.id, pockets.get(+this.id) + +quantity)
    }
    else {
        pockets.set(+this.id, +quantity)
    }
    $(".add-alert").show()
    console.log("Added " + quantity + " pockets with id = " + this.id);
});


/*Priceholders section slide and add to virtual cart*/
$(".priceholder").click(function () {
    $(".priceholders").slideToggle("fast");
});

$(".priceholders").find(".button").click(function () {
    let quantity = $(".priceholder_module").find(`input[form=${this.id}]`).val();
    if (quantity === "") {
        quantity = 0
    }
    if (priceholders.has(+this.id)) {
        priceholders.set(+this.id, priceholders.get(+this.id) + +quantity)
    }
    else {
        priceholders.set(+this.id, +quantity)
    }
    console.log("Added " + quantity + " priceholders with id = " + this.id);
});


/*Plasticholders section slide and add to virtual cart*/
$(".plasticholder").click(function () {
    $(".plasticholders").slideToggle("fast");
});

$(".plasticholders").find(".button").click(function () {
    let quantity = $(".plasticholder_module").find(`input[form=${this.id}]`).val();
    if (quantity === "") {
        quantity = 0
    }
    if (plasticholders.has(+this.id)) {
        plasticholders.set(+this.id, plasticholders.get(+this.id) + +quantity)
    }
    else {
        plasticholders.set(+this.id, +quantity)
    }
    console.log("Added " + quantity + " plasticholders with id = " + this.id);
});


/*Pricepapers section slide and add to virtual cart*/
$(".pricepaper").click(function () {
    $(".pricepapers").slideToggle("fast");
});

$(".pricepapers").find(".button").click(function () {
    let quantity = $(".pricepaper_module").find(`input[form=${this.id}]`).val();
    if (quantity === "") {
        quantity = 0
    }
    if (pricepapers.has(+this.id)) {
        pricepapers.set(+this.id, pricepapers.get(+this.id) + +quantity)
    }
    else {
        pricepapers.set(+this.id, +quantity)
    }
    console.log("Added " + quantity + " pricepapers with id = " + this.id);
});


/*Others section slide and add to virtual cart*/
$(".other").click(function () {
    $(".others").slideToggle("fast");
});

$(".others").find(".button").click(function () {
    let quantity = $(".other_module").find(`input[form=${this.id}]`).val();
    if (quantity === "") {
        quantity = 0
    }
    if (others.has(+this.id)) {
        others.set(+this.id, others.get(+this.id) + +quantity)
    }
    else {
        others.set(+this.id, +quantity)
    }
    console.log("Added " + quantity + " others with id = " + this.id);
});






 /*   $("#id_bar_code").change(function (e) {
        e.preventDefault();
        // get the bar_code
        const bar_code = $(this).val();
        let readonly = true;

        // GET AJAX request
        $.ajax({
            type: 'GET',
            url: "{% url 'search' %}",
            data: {"bar_code": bar_code},
            success: function (response) {
                // Товар найден в БД
                if (response["success"]) {
                    const bar_code = $("#id_bar_code");
                    const lm_code = $("#id_lm_code");
                    const caption = $("#id_caption");
                    const amount_goods = $("#id_amount_goods");

                    let instance = response["catalog"];

                    bar_code.val(instance["ean"]);
                    lm_code.val(instance["lm"]);
                    caption.val(instance["product_name"]);
                    {#console.log(instance)#}
                    {#console.log(instance["ean"])#}
                    {#console.log(instance["lm"])#}
                    {#console.log(instance["product_name"])#}
                    lm_code.attr('readonly', readonly);
                    caption.attr('readonly', readonly);
                    amount_goods.focus()


                }  //end if
            }, // close if success
            // ТОВАР
            error: function (response) {
                const bar_code = $("#id_bar_code");
                alert("Товар не найден");
                $("#ADD-post-form").trigger('reset');
                bar_code.focus()
                console.log(response)
            } // close if error
        })   // close ajax
    }) // close function


}) // close  $(document).ready
</script>
{% endblock javascript %}
*/