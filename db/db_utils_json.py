class JSONPolicyDatabase:
    def __init__(self):
        self.policies = []
        self.policy_types = []
        self.load_initial_data()

    def load_initial_data(self):
        default_data = [
            {"id": 1, "name": "Secure Future Term Life", "type": "Term Life", "premium": 5000, "coverage": 1000000},
            {"id": 2, "name": "Health Shield Plan", "type": "Health", "premium": 3000, "coverage": 500000},
            {"id": 3, "name": "Car Protect Plan", "type": "Vehicle", "premium": 2000, "coverage": 300000},
            {"id": 4, "name": "Family Health Plus", "type": "Health", "premium": 4500, "coverage": 750000},
            {"id": 5, "name": "Premium Vehicle Cover", "type": "Vehicle", "premium": 3500, "coverage": 600000},
            {"id": 6, "name": "Senior Life Protection", "type": "Term Life", "premium": 6500, "coverage": 1200000},
            {"id": 7, "name": "Basic Health Care", "type": "Health", "premium": 1800, "coverage": 300000},
            {"id": 8, "name": "Two-Wheeler Insurance", "type": "Vehicle", "premium": 1200, "coverage": 150000},
            {"id": 9, "name": "Child Education Plan", "type": "Term Life", "premium": 4000, "coverage": 800000},
            {"id": 10, "name": "Comprehensive Health", "type": "Health", "premium": 5500, "coverage": 900000}
        ]
        
        self.policies = default_data
        
        self.policy_types = list(set(item["type"] for item in default_data))
    
    def get_all_policies(self):
        return self.policies
    
    def get_filtered_policies(self, search_term=None, min_premium=None, max_premium=None, 
                             policy_type=None, min_coverage=None, sort_by=None, sort_direction=None):

        filtered_policies = self.policies.copy()

        # Apply filters
        if search_term is not None:
            search_term_lower = search_term.lower()
            filtered_policies = [p for p in filtered_policies if search_term_lower in p['name'].lower()]
        
        if min_premium is not None:
            filtered_policies = [p for p in filtered_policies if p['premium'] >= min_premium]
      
        
        if max_premium is not None:
            filtered_policies = [
                p for p in filtered_policies 
                if float(p['premium']) <= float(max_premium)
            ]

        if str(policy_type).lower() != "all":
            filtered_policies = [p for p in filtered_policies if p['type'].lower() == policy_type.lower()]
        
     
        if min_coverage is not None:
            filtered_policies = [
                p for p in filtered_policies if float(p["coverage"]) >= float(min_coverage)
            ]
        # Apply sorting
        if sort_by == 'premium':
            reverse = sort_direction == 'desc'
            filtered_policies.sort(key=lambda p: p['premium'], reverse=reverse)
        
        return filtered_policies
    
    def get_policy_types(self):
        return sorted(self.policy_types)
    
