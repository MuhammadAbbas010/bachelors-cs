
// DATA & STATE STORE
const staffData = [
  { id: 1, name: "Ms. Rao", department: "Math Dept." },
  { id: 2, name: "Mr. Chen", department: "Math Dept." },
  { id: 3, name: "Mrs. Smith", department: "English Dept." },
  { id: 4, name: "Dr. Adams", department: "Science Dept." }
];

const slotData = [
  { id: "slot1", time: "9:00 AM", status: "available" },
  { id: "slot2", time: "9:30 AM", status: "booked" },
  { id: "slot3", time: "10:00 AM", status: "available" },
  { id: "slot4", time: "10:30 AM", status: "available" },
  { id: "slot5", time: "11:00 AM", status: "available" },
  { id: "slot6", time: "11:30 AM", status: "booked" }
];

const topicParagraphs = {
  general: "General progress and overall academic development next steps.",
  behavior: "Classroom behavior, agreed routines, and support frameworks.",
  academic: "Bring recent assignment scores and class notes so we can discuss the learning plan."
};

let selectedStaff = null;
let selectedTime = null;
let currentStep = 0;
const totalSteps = 3;


// DOM ELEMENT REFERENCES
const staffGrid = document.getElementById("staff-grid");
const staffSearch = document.getElementById("staff-search");
const emptyMsg = document.getElementById("empty-msg");

const appointmentForm = document.getElementById("appointment-form");
const parentName = document.getElementById("parent-name");
const parentEmail = document.getElementById("parent-email");
const preferredDate = document.getElementById("preferred-date");
const selectedStaffDisplay = document.getElementById("selected-staff-display");

const emailError = document.getElementById("email-error");
const dateError = document.getElementById("date-error");
const nameError = document.getElementById("name-error");
const staffError = document.getElementById("staff-error");

const slotGrid = document.getElementById("slot-grid");
const slotConfirmation = document.getElementById("slot-confirmation");

const meetingTopic = document.getElementById("meeting-topic");
const finalMessage = document.getElementById("final-message");
const finishBtn = document.getElementById("finish-btn");

const progressFill = document.getElementById("progress-fill");
const progressLabel = document.getElementById("progress-label");
const progressTrack = document.getElementById("progress-track");
const step1Badge = document.getElementById("step1-badge");
const step2Badge = document.getElementById("step2-badge");
const step3Badge = document.getElementById("step3-badge");


// INITIALIZATION
document.addEventListener("DOMContentLoaded", () => {
  renderStaffCards(staffData);
  renderSlotButtons(slotData);
  updateProgress();
});

// TASK 5: DERIVED PROGRESS STATE
function updateProgress() {
  const pct = Math.min(100, Math.round((currentStep / totalSteps) * 100));
  progressFill.style.width = `${pct}%`;
  progressTrack.setAttribute("aria-valuenow", pct);

  let actionText = "Select Staff & Details";
  if (currentStep === 1) actionText = "Select Time Slot";
  if (currentStep === 2) actionText = "Confirm Details";
  if (currentStep === 3) actionText = "Completed";

  progressLabel.textContent = `Progress: ${pct}% Complete (${actionText})`;

  // Update visual badges
  step1Badge.classList.toggle("active", currentStep >= 1);
  step2Badge.classList.toggle("active", currentStep >= 2);
  step3Badge.classList.toggle("active", currentStep >= 3);
}


// TASK 3: REAL-TIME STAFF DIRECTORY FILTERING
function renderStaffCards(data) {
  staffGrid.innerHTML = "";
  data.forEach(person => {
    const card = document.createElement("div");
    card.className = `staff-card ${selectedStaff?.id === person.id ? "selected" : ""}`;
    card.setAttribute("tabindex", "0");
    card.innerHTML = `
      <h3>${person.name}</h3>
      <p>${person.department}</p>
    `;

    card.addEventListener("click", () => selectStaffMember(person));
    card.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        selectStaffMember(person);
      }
    });

    staffGrid.appendChild(card);
  });
}

function selectStaffMember(person) {
  selectedStaff = person;
  selectedStaffDisplay.value = `${person.name} (${person.department})`;
  selectedStaffDisplay.classList.remove("invalid");
  staffError.textContent = "";
  renderStaffCards(getFilteredStaff());
  updateConfirmationText();
}

function getFilteredStaff() {
  const query = staffSearch.value.trim().toLowerCase();
  return staffData.filter(p => 
    `${p.name} ${p.department}`.toLowerCase().includes(query)
  );
}

staffSearch.addEventListener("input", () => {
  const filtered = getFilteredStaff();
  renderStaffCards(filtered);
  emptyMsg.hidden = filtered.length !== 0;
});


// TASK 1: APPOINTMENT FORM VALIDATION
appointmentForm.addEventListener("submit", (e) => {
  e.preventDefault();
  let isValid = true;

  // Clear errors
  nameError.textContent = "";
  emailError.textContent = "";
  dateError.textContent = "";
  staffError.textContent = "";
  parentName.classList.remove("invalid");
  parentEmail.classList.remove("invalid");
  preferredDate.classList.remove("invalid");
  selectedStaffDisplay.classList.remove("invalid");

  // Validate Name
  if (!parentName.value.trim()) {
    nameError.textContent = "Error: Please enter parent name.";
    parentName.classList.add("invalid");
    isValid = false;
  }

  // Validate Email via Constraint API
  if (!parentEmail.checkValidity() || !parentEmail.value.trim()) {
    emailError.textContent = "Error: Please enter a valid email address.";
    parentEmail.classList.add("invalid");
    isValid = false;
  }

  // Validate Date (Not in the past)
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const selectedDate = new Date(preferredDate.value);

  if (!preferredDate.value || selectedDate < today) {
    dateError.textContent = "Error: Date must not be in the past.";
    preferredDate.classList.add("invalid");
    isValid = false;
  }

  // Validate Staff Selection
  if (!selectedStaff) {
    staffError.textContent = "Error: Please select a staff member above.";
    selectedStaffDisplay.classList.add("invalid");
    isValid = false;
  }

  if (isValid) {
    if (currentStep < 1) currentStep = 1;
    updateProgress();
    document.getElementById("slots-section").scrollIntoView({ behavior: "smooth" });
  }
});

// ==========================================================================
// TASK 2: TIME-SLOT STATE MACHINE
function renderSlotButtons(slots) {
  slotGrid.innerHTML = "";
  slots.forEach(slot => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = `slot ${slot.status}`;
    btn.textContent = slot.time;
    btn.dataset.time = slot.time;
    btn.dataset.status = slot.status;

    if (slot.status === "booked") {
      btn.disabled = true;
    }

    slotGrid.appendChild(btn);
  });
}

// Delegated Click Listener
slotGrid.addEventListener("click", (e) => {
  const btn = e.target.closest("button.slot");
  if (!btn || btn.classList.contains("booked")) return;

  // Clear existing selections
  document.querySelectorAll(".slot.selected").forEach(s => s.classList.remove("selected"));

  // Apply new state
  btn.classList.add("selected");
  selectedTime = btn.dataset.time;

  const staffName = selectedStaff ? selectedStaff.name : "Selected Staff";
  slotConfirmation.textContent = `Appointment Confirmed: ${selectedTime} with ${staffName}.`;

  if (currentStep < 2) currentStep = 2;
  updateProgress();
  updateConfirmationText();
});

// ==========================================================================
// TASK 4: CONFIRMATION COMPOSER
meetingTopic.addEventListener("change", () => {
  updateConfirmationText();
});

function updateConfirmationText() {
  const topicKey = meetingTopic.value;
  if (!topicKey) return;

  const staffName = selectedStaff ? selectedStaff.name : "the staff member";
  const timeStr = selectedTime ? ` at ${selectedTime}` : "";
  const dateStr = preferredDate.value ? ` on ${preferredDate.value}` : "";
  const paragraph = topicParagraphs[topicKey] || "";

  finalMessage.value = `Thank you for scheduling. Your meeting with ${staffName}${timeStr}${dateStr} will focus on ${meetingTopic.options[meetingTopic.selectedIndex].text}. ${paragraph}`;
}

finishBtn.addEventListener("click", () => {
  if (!selectedStaff || !selectedTime || !meetingTopic.value) {
    alert("Please complete all fields, select a time slot, and pick a meeting topic.");
    return;
  }

  currentStep = 3;
  updateProgress();
  alert("Appointment successfully booked and confirmed!");
});