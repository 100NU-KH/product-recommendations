from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from products.models import Product


class Recommender:
    
    def get_similar_products(self, prodcut_id: int, top_n=10):
        vectorizer = TfidfVectorizer(stop_words="english")
        product_descriptions = Product.objects.all().values_list('description', flat=True)
        tfid_matrix = vectorizer.fit_transform(product_descriptions)
        target_item = Product.objects.get(id = prodcut_id)
        
        all_products = list(Product.objects.all())
        print("########target_item", all_products)
        target_index = all_products.index(target_item)
        print("-----------", target_index)
        cosine_sim_obj = cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
        print("```````````", cosine_sim_obj)
        similarIndex_products_ = cosine_sim_obj.argsort()[-(top_n-1): -1][::-1]
        print("[[[[[[[[[[[]]]]]]]]]]]   ", similarIndex_products_)
        similarIndex_products = [item_indx for item_indx in similarIndex_products_]
        print(similarIndex_products)
        similar_products = list()
        for idx in similarIndex_products:
            similar_products.append(all_products[idx])
        
        return similar_products