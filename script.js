let adjectives = [
    ["RISES", "SOARS", "SHOOTS UP", "SURGES", "HIKES"],
    ["TANKS", "PLUMMETS", "NOSEDIVES", "CRASHES", "PLUNGES"],
];

let rise_or_fall = Math.round(Math.random());
let chosen_adjective =
    adjectives[rise_or_fall][
        Math.floor(adjectives[rise_or_fall].length * Math.random())
    ];

document.getElementById("stonk-state").innerHTML = chosen_adjective;

fetch("https://newsapi.org/v2/top-headlines?language=en", {
    headers: { "X-Api-Key": "8ea847ede21a429ab8e00cf40c3199af" },
})
    .then((data) => data.json())
    .then((res) => {
        document.getElementById("headline").innerHTML =
            res["articles"][0]["title"];
    });
