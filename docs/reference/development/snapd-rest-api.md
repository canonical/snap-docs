# SnapD REST API

The REST API provides access to snapd's state and many of its key functions, as listed below.

For general information on how to use the API, including how to access it, its requests and responses, results fields and error types, see [Using the REST API](/how-to-guides/snap-development/use-the-rest-api).

## API endpoints

<link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui.css" ></link>
<link rel="stylesheet" type="text/css" href="../../../_static/swagger-override.css" ></link>
<div id="swagger-ui"></div>

<script src="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui-bundle.js" charset="UTF-8" crossorigin> </script>
<script src="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui-standalone-preset.js" charset="UTF-8 crossorigin"> </script>
<script>
window.onload = function() {
  // Begin Swagger UI call region
  const ui = SwaggerUIBundle({
//    url: 'https://snapcraft.io/docs/reference/development/openapi.yaml',
//    url: '/docs/openapi.json',
    url: window.location.pathname +"../../../openapi.yaml",
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [],
    validatorUrl: "none",
    defaultModelsExpandDepth: -1,
    supportedSubmitMethods: []
  })
  // End Swagger UI call region

  window.ui = ui

  function addSwaggerTagsToTOC(tags) {
    // Find the last H2 entry in the TOC and insert a 'ul' element for the tag list
    const tocContainer = document.querySelector(
      ".toc-tree > ul > li > ul > li:last-child"
    );
    const tocList = document.createElement("ul");
    tocContainer.appendChild(tocList);
    // Add a link for each tag inside the 'ul' element
    for (const tag of tags) {
      // Create an 'a' element for the tag link
      const tocLink = document.createElement("a");
      tocLink.classList.add("reference", "internal");
      const urlFriendlyTag = tag.replace(/ /g, "-");
      tocLink.href = `#/${urlFriendlyTag}`;
      tocLink.innerText = tag;
      tocLink.addEventListener("click", event => {
        if (event.shiftKey || event.ctrlKey || event.altKey || event.metaKey) {
          return;
        }
        // When the tag link is clicked with no modifier keys:
        // - Scroll the tag section into view
        // - If the tag section is closed, open it (by simulating a click)
        const operationsTag = tag.replace(/ /g, "_");
        const swaggerHeading = document.getElementById(`operations-tag-${operationsTag}`);
        swaggerHeading.scrollIntoView({
          behavior: "smooth"
        });
        if (swaggerHeading.getAttribute("data-is-open") == "false") {
          swaggerHeading.click();
        }
      });
      // Wrap the tag link in a 'li' element and add it to the tag list
      const tocItem = document.createElement("li");
      tocItem.appendChild(tocLink);
      tocList.appendChild(tocItem);
    }
  }

  // Make sure to match the tags defined in openapi.yaml
  addSwaggerTagsToTOC([
  "Assertions",
  "Asynchronous",
  "AuthenticationRequired",
  "Changes",
  "Experimental",
  "Interfaces",
  "Notices",
  "OpenAccess",
  "Prompting",
  "Root",
  "Snaps",
  "Store",
  "Synchronous",
  "Systems",
  "Users",
  "Validation Sets",
  "Warnings"
  ]);
}
</script>

