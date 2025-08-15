import React from 'react';
import Layout from '@theme/Layout';

export default function Hello() {
  React.useEffect(() => {
    const script = document.createElement('script');
    script.src = "https://giscus.app/client.js";
    script.setAttribute("data-repo", "Xiang511/RUNNING-WITH-RIFLES");
    script.setAttribute("data-repo-id", "R_kgDOPbpSUA");
    script.setAttribute("data-category", "Announcements");
    script.setAttribute("data-category-id", "DIC_kwDOPbpSUM4CuN3v");
    script.setAttribute("data-mapping", "pathname");
    script.setAttribute("data-strict", "0");
    script.setAttribute("data-reactions-enabled", "0");
    script.setAttribute("data-emit-metadata", "0");
    script.setAttribute("data-input-position", "bottom");
    script.setAttribute("data-theme", "light");
    script.setAttribute("data-lang", "en");
    script.setAttribute("crossorigin", "anonymous");
    script.async = true;
    const giscusContainer = document.getElementById('giscus_container');
    if (giscusContainer) {
      giscusContainer.appendChild(script);
    }
    return () => {
      if (giscusContainer) {
        giscusContainer.innerHTML = "";
      }
    };
  }, []);

  return (
    <Layout title="Discussions" description="Discussions">
      <div id="giscus_container" style={{
          width: '80%',
          margin: 'auto',
          padding: '1.5em 0 ',
        }}></div>
    </Layout>
  );
}