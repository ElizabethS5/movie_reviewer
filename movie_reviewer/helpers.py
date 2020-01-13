from movie_reviewer.reviews.models import Review


def get_review_recommendation_breakdown_dictionary(movie):
    all_reviews_of_movie = Review.objects.filter(movie=movie)
    pro_reviews = 0
    unpro_reviews = 0
    positive_pro_reviews = 0
    positive_unpro_reviews = 0
    for review in all_reviews_of_movie:
        if review.critic.pro:
            pro_reviews += 1
            if review.recommend:
                positive_pro_reviews += 1
        else:
            unpro_reviews += 1
            if review.recommend:
                positive_unpro_reviews += 1
    review_dict = {
        'num_all': len(all_reviews_of_movie),
        'num_positive': positive_pro_reviews + positive_unpro_reviews,
        'num_all_professional': pro_reviews,
        'num_positive_professional': positive_pro_reviews,
        'num_all_unprofessional': unpro_reviews,
        'num_positive_unprofessional': positive_unpro_reviews
    }
    return review_dict


def get_combined_reviews_percentage(movie):
    if not movie:
        return 'No reviews'
    all_reviews = Review.objects.filter(movie=movie)
    if not all_reviews:
        return 'No reviews'
    all_positive_reviews = [
        review for review in all_reviews if review.recommend]
    decimal = len(all_positive_reviews) / len(all_reviews)
    return f'{round(decimal * 100, 1)}%'


def get_professional_reviews_percentage(movie):
    if not movie:
        return 'No professional reviews'
    all_reviews = Review.objects.filter(movie=movie)
    if not all_reviews:
        return 'No professional reviews'
    professional_reviews = [
        review for review in all_reviews if review.critic.professional]
    if not professional_reviews:
        return 'No professional reviews'
    postive_professional_reviews = [
        review for review in professional_reviews if review.recommend
    ]
    decimal = len(postive_professional_reviews) / len(professional_reviews)
    return f'{round(decimal * 100, 1)}%'


def get_unprofessional_reviews_percentage(movie):
    if not movie:
        return 'No audience reviews'
    all_reviews = Review.objects.filter(movie=movie)
    if not all_reviews:
        return 'No audience reviews'
    unprofessional_reviews = [
        review for review in all_reviews if not review.critic.professional]
    if not unprofessional_reviews:
        return 'No audience reviews'
    postive_unprofessional_reviews = [
        review for review in unprofessional_reviews if review.recommend
    ]
    decimal = len(postive_unprofessional_reviews) / len(unprofessional_reviews)
    return f'{round(decimal * 100, 1)}%'
