function showQuestion(questionText, options) {
    const panel = document.querySelector("#panel");
    panel.innerHTML = "";

    const p = document.createElement("p");
    p.textContent = questionText;
    panel.appendChild(p);

    options.forEach(option => {
        const btn = document.createElement("button");
        btn.textContent = option.text;
        btn.addEventListener("click", option.callback);
        panel.appendChild(btn);
    });
}

