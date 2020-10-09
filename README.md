# tcc
TCC Computer Aided Molecular Design Aromatic Substances

Contém os arquivos utilizados para a elaboração do Trabalho de Conclusão do Curso de Eng. Química na Universidade de São Paulo elaborado por Arthur A. de Camargo e Pedro A. Eggers.

Bibliotecas externas utilizadas:
  - pubchempy: interação com o banco de dados do PubChem
  - xlsxwriter: criação do arquivo .xlsx para alimentar o banco de dados
  - selenium: navegação e leitura de páginas do site do PubChem para obter dados que não estão disponíveis via pubchempy
  
Arquivos:
  - app.py: arquivo contendo as classes relacionadas à interface gráfica (executar esse para ver o funcionamento do programa).

  - camd_db.db: arquivo do banco de dados de propriedades dos compostos. Para ver de fato o banco de dados, recomendo baixar o SQLiteStudio.

  - chromedriver: arquivo necessário para que o selenium consiga acessar o site do PubChem via Chrome.

  - get_properties.py: arquivo usado para o web-scraping do site do PubChem para dados do PubChem não acessíveis via pubchempy. Caso queiram rodar, é necessário mudar o local dos arquivos "Properties.csv" e "chromedriver" no código, uma vez que eles estão especificados para o computador do Pedro.

  - import_pubchem.py: arquivo usado para obter e exportar em .xlsx os dados do PubChem acessíveis via pubchempy.
  
  - query.py: arquivo utilizado para interações com o banco de dados camd_db.db;
  
  
