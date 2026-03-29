## 产品分类

{{ $categories := slice }}
{{ range .Site.Pages }}
  {{ if eq .Section "products" }}
    {{ with .Params.categories }}
      {{ $categories = $categories | append (index . 0) }}
    {{ end }}
  {{ end }}
{{ end }}
{{ $uniqueCategories := $categories | uniq }}
<div class="category-cloud" style="margin-top: 2rem; text-align: center;">
  {{ range $uniqueCategories }}
    <a href="/categories/{{ . | urlize }}" 
       style="display: inline-block; margin: 0.5rem; padding: 0.3rem 0.8rem; 
              background: #f0f0f0; border-radius: 20px; text-decoration: none; 
              font-size: 1rem; color: #333;">
      {{ . }}
    </a>
  {{ end }}
</div>