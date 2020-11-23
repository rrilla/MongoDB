package com.example.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.domain.Board;
import com.example.demo.service.BoardService;

@Controller
@RequestMapping("/board")
public class BoardController {

	@Autowired
	BoardService boardService;
	
	@GetMapping({"/main","/list"})
	public String main(Model model) {
		model.addAttribute("boards", boardService.main());
		return "list";
	}
	
	@GetMapping("/register")
	public String register() {
		return "register";
	}
	
	@PostMapping("/register")
	public String register2(Board board) {
		System.out.println(1);
		boardService.register(board);
		System.out.println(2);
		return "redirect:/board";
	}
	
	@GetMapping("/detail/{id}")
	public String detail(@PathVariable String id, Model model) {
		System.out.println(id);
		Board board = boardService.detail(id);
		System.out.println(board.getTitle());
		model.addAttribute("board", board);
		
		return "detail";
	}
	
}
