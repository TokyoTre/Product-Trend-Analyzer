test_cases = [
    # 1. Validate schema
    (
        'validate_schema', 
        ['problems/product_trend_analyzer/input_cases/product_trend_analyzer_sales_data.csv'], 
        {'fatal': False, 'errors': []}  # Expect no fatal errors now that all columns exist
    ),

    # 2. Trend detection
    (
        'detect_trend_candidates', 
        ['problems/product_trend_analyzer/input_cases/product_trend_analyzer_sales_data.csv', ['prod_1', 'prod_2', 'prod_3'], 30],
        [
            {'product_id': 'prod_1', 'is_spike_candidate': False, 'reason_tags': [], 'velocity_pct_change_min': 0.0, 'confidence_score_min': 0.0},
            {'product_id': 'prod_2', 'is_spike_candidate': False, 'reason_tags': [], 'velocity_pct_change_min': 0.0, 'confidence_score_min': 0.0},
            {'product_id': 'prod_3', 'is_spike_candidate': False, 'reason_tags': [], 'velocity_pct_change_min': 0.0, 'confidence_score_min': 0.0}
        ]
    ),

    # 3. Supplier ranking
    (
        'rank_suppliers_for_product', 
        ['prod_1', 'problems/product_trend_analyzer/input_cases/product_trend_analyzer_sales_data.csv'],
        {'product_id': 'prod_1', 'top_supplier': {'supplier_id': 'sup_1', 'rank_score_min': 0, 'lead_time_days_max': 0}}
    ),

    # 4. Pricing recommendation
    (
        'recommend_pricing', 
        ['prod_1', 20.0, 100, 'problems/product_trend_analyzer/input_cases/product_trend_analyzer_sales_data.csv'],
        {'product_id': 'prod_1', 'suggested_price_conservative_min': 0.0, 'suggested_price_aggressive_max': 0.0, 'target_margin_pct': 20.0}
    )
]


