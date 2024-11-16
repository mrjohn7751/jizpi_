document.addEventListener("DOMContentLoaded", function () {
  const paragraphs = document.querySelectorAll(".paragraph");
  const maxLength = 60;
  const maxUnderscoreLength = 40;

  paragraphs.forEach((paragraph) => {
    let textLength = paragraph.textContent.length;

    if (textLength > maxLength) {
      let truncatedText = paragraph.textContent.substring(0, maxLength - 1);
      let words = truncatedText.split(" ");
      words.pop();
      truncatedText = words.join(" ");
      paragraph.textContent = truncatedText + "...";
    } else if (textLength < maxUnderscoreLength) {
      const undersCount = maxUnderscoreLength - textLength;
      paragraph.textContent += ".".repeat(undersCount);
    }
    if (paragraph.textContent.length < maxLength) {
      const missingCount = maxLength - paragraph.textContent.length;
      paragraph.textContent += ".".repeat(missingCount);
    }
    const wordsArray = paragraph.textContent.split(" ");
    wordsArray.forEach((word, index) => {
      if (word.length > 8) {
        const halfLength = Math.ceil(word.length / 2);
        wordsArray[index] =
          word.substring(0, halfLength) + " " + word.substring(halfLength);
      }
    });
    paragraph.textContent = wordsArray.join(" ");
  });

  const cardsPerPage = 16;
  const cardContainer = document.getElementById("cardContainer");
  const cards = document.querySelectorAll(".info-card");
  const prevPageLink = document.getElementById("prevPage");
  const nextPageLink = document.getElementById("nextPage");

  let currentPage = 1;

  function showPage(page) {
    const startIndex = (page - 1) * cardsPerPage;
    const endIndex = page * cardsPerPage;

    cards.forEach((card, index) => {
      if (index >= startIndex && index < endIndex) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });

    if (page > 1) {
      cardContainer.classList.add("align-right");
    } else {
      cardContainer.classList.remove("align-right");
    }
  }

  function updatePaginationButtons() {
    const totalPages = Math.ceil(cards.length / cardsPerPage);

    const paginationLinks = document.querySelectorAll(".pagination-link");
    paginationLinks.forEach((link) => {
      link.parentNode.removeChild(link);
    });

      const displayPages = [];
    const maxDisplayPages = Math.min(totalPages, 4);
    const halfMaxDisplayPages = Math.ceil(maxDisplayPages / 2);
    let startPage = Math.max(currentPage - halfMaxDisplayPages, 1);
    let endPage = Math.min(startPage + maxDisplayPages - 1, totalPages);
    if (endPage - startPage < maxDisplayPages - 1) {
      startPage = Math.max(endPage - maxDisplayPages + 1, 1);
    }
    for (let i = startPage; i <= endPage; i++) {
      displayPages.push(i);
    }

    displayPages.forEach((page) => {
      const pageLink = document.createElement("a");
      pageLink.href = "#";
      pageLink.textContent = page;
      pageLink.classList.add("pagination-link");
      pageLink.addEventListener("click", function (event) {
        event.preventDefault();
        currentPage = page;
        showPage(currentPage);
        updatePaginationButtons();
      });
      if (page === currentPage) {
        pageLink.classList.add("active");
      }
      nextPageLink.parentNode.insertBefore(pageLink, nextPageLink);
    });

    if (currentPage === 1) {
      prevPageLink.style.display = "none";
    } else {
      prevPageLink.style.display = "inline";
    }

    if (currentPage === totalPages) {
      nextPageLink.style.display = "none";
    } else {
      nextPageLink.style.display = "inline";
    }
  }

  function handlePrevPageClick(event) {
    event.preventDefault();
    if (currentPage > 1) {
      currentPage--;
      showPage(currentPage);
      updatePaginationButtons();
    }
  }

  function handleNextPageClick(event) {
    event.preventDefault();
    const totalPages = Math.ceil(cards.length / cardsPerPage);
    if (currentPage < totalPages) {
      currentPage++;
      showPage(currentPage);
      updatePaginationButtons();
    }
  }

  prevPageLink.addEventListener("click", handlePrevPageClick);
  nextPageLink.addEventListener("click", handleNextPageClick);

  showPage(currentPage);
  updatePaginationButtons();
});
