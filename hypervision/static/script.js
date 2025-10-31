(function () {
  try {
    const radios = Array.from(document.querySelectorAll('input[name="problem_id"]'));
    const labels = new Map();
    radios.forEach((r) => {
      const label = document.querySelector(`label[for="${r.id}"]`);
      if (label) labels.set(r, label);
    });

    function update() {
      labels.forEach((label) => label.classList.remove('selected'));
      const checked = radios.find((r) => r.checked);
      if (checked && labels.has(checked)) labels.get(checked).classList.add('selected');
    }

    radios.forEach((r) => r.addEventListener('change', update));
    update();
  } catch (e) {
  }
})();


