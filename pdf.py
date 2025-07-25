from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "7-Day Meal Plan & Progress Tracker", ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, "Customized for: Female, 53 y/o | 148 cm | 62 kg | Goals: Weight loss, energy, no bloating", ln=True, align="C")
        self.ln(5)
    
    def chapter_title(self, day):
        self.set_font("Arial", "B", 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 8, f"Day {day}", ln=True, fill=True)
    
    def chapter_body(self, meals):
        self.set_font("Arial", "", 11)
        for meal, content in meals.items():
            self.set_font("Arial", "B", 11)
            self.cell(0, 8, f"{meal}:", ln=True)
            self.set_font("Arial", "", 11)
            self.multi_cell(0, 8, f"{content}")
        self.ln(3)

    def progress_tracker(self):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Weekly Progress Tracker", ln=True)
        self.set_font("Arial", "", 11)
        tracker_items = [
            "- Weight (check once a week in the morning before breakfast)",
            "- Daily bloating check: (None / Mild / Moderate / Severe)",
            "- Daily energy level: (Scale 1-5)",
            "- Notes (e.g., digestion, mood, sleep)"
        ]
        for item in tracker_items:
            self.cell(0, 8, item, ln=True)
        self.ln(5)
        self.cell(0, 8, "Day | Weight | Bloating | Energy | Notes", ln=True)
        for i in range(1, 8):
            self.cell(0, 8, f"{i}   |         |           |        |", ln=True)
        self.ln(10)
        self.cell(0, 8, "Tips: Avoid shellfish, pineapple, citrus. Stay hydrated. Eat slowly. Walk 20-30 mins daily.", ln=True)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

meal_plan = {
    1: {
        "9 AM (Break-fast)": "Chia pudding with almond milk, ½ banana, flaxseed. Green tea or warm ginger water.",
        "1 PM (Lunch)": "Grilled salmon, steamed broccoli, ½ cup quinoa, olive oil dressing.",
        "6 PM (Light dinner)": "1 boiled egg, cucumber salad with avocado and pumpkin seeds."
    },
    2: {
        "9 AM": "Scrambled eggs (2) with spinach and mushrooms. 1 slice whole grain toast. Herbal tea.",
        "1 PM": "Chicken stir-fry with olive oil, broccoli, bell peppers. ½ cup brown rice.",
        "6 PM": "Greek yogurt with chia seeds and blueberries."
    },
    3: {
        "9 AM": "Smoothie: ½ banana, spinach, protein powder, almond milk.",
        "1 PM": "Lentil soup with steamed greens and 1 boiled sweet potato.",
        "6 PM": "Tuna salad with olive oil, mixed greens, and 1 boiled egg."
    },
    4: {
        "9 AM": "Oats with chia seeds, cinnamon, chopped apples. Peppermint tea.",
        "1 PM": "Grilled chicken, roasted zucchini, ½ avocado, mixed greens.",
        "6 PM": "Vegetable omelet (2 eggs) with steamed broccoli."
    },
    5: {
        "9 AM": "Greek yogurt with sunflower seeds and kiwi slices.",
        "1 PM": "Grilled fish, roasted cauliflower, ½ cup quinoa.",
        "6 PM": "Soup: zucchini, carrots, lentils + side salad."
    },
    6: {
        "9 AM": "1 boiled egg, cucumber sticks, 1 slice toast. Ginger tea.",
        "1 PM": "Tofu or grilled chicken wrap in lettuce with hummus and cucumber.",
        "6 PM": "Berry bowl with coconut flakes and chia seeds."
    },
    7: {
        "9 AM": "Smoothie bowl: blended berries, almond milk, chia seeds, topped with nuts.",
        "1 PM": "Grilled turkey patties, sautéed kale, roasted carrots.",
        "6 PM": "Baked eggplant slices with tomato-free herb dressing and feta (optional)."
    }
}

for day, meals in meal_plan.items():
    pdf.chapter_title(day)
    pdf.chapter_body(meals)

pdf.progress_tracker()
pdf.output("7-Day_Meal_Plan_and_Tracker.pdf")